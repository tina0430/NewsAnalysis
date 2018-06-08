
date_e<-'20180430'
period<-c(90:365)
per_result<-data.frame(period=c(0),lm_val=c(0),lm_val2=c(0),lm_test=c(0),rf_val=c(0),rf_val2=c(0),rf_test=c(0))
count_p<-1
for (p in period){
  cat('NO :',count_p,'period :',p,'m start\n')
  #dataset 추출 
  subDataSet<-subset_merge(date_e)
  #주말연휴데이터 처리
  wtestset<-subDataSet
  w_idx <- which(wtestset[1,]=='w')
  wtestset<-wtestset[,-w_idx]
  #행렬치환 
  AnalDF<- tdataset(wtestset)
  #NA -> 0
  AnalDF[is.na(AnalDF)] <- 0
  
  fname<-paste('result_csv/AnalDF',count_p,'.csv')
  fname<-str_replace_all(fname,' ','')
  write.csv(AnalDF,fname,quote = F, row.names = T)
  
  cat('NO :',count_p,'period :',p,'A start\n')
  
  #tmp1 (상관계수 삭제 )
  data<-AnalDF
  tmp <- as.data.frame(cor(data[,-1], as.numeric(data$class)))
  tmp <- na.omit(tmp)
  tmp <- subset(tmp, V1>=0.1 | V1<=-0.1)
  tmp <- tmp %>% rename(cor=V1)
  tmp$var <- rownames(tmp)
  data_mody <- data[,tmp$var]
  names(data_mody)[1] <- 'class'
  data_mody$class <- factor(data$class)
  data<-data_mody
  
  #tmp2 (상관계수 삭제 안함  )
  data2<-AnalDF
  tmp2 <- as.data.frame(cor(data2[,-1], as.numeric(data2$class)))
  tmp2 <- na.omit(tmp2)
  tmp2 <- tmp2 %>% rename(cor=V1)
  tmp2$var <- rownames(tmp2)
  data2_mody <- data2[,tmp2$var]
  names(data2_mody)[1] <- 'class'
  data2_mody$class <- factor(data2$class)
  data2<-data2_mody
  
  # training, validation
  set.seed(1606)
  n<-nrow(data)
  idx <- c(1:n)
  training_idx <- sample(idx, n *0.7)
  validate_idx <- setdiff(idx, training_idx)
  training <- data[training_idx,]
  validation <- data[validate_idx,]
  
  # training, validation2
  set.seed(1607)
  n2<-nrow(data2)
  idx2 <- c(1:n2)
  training_idx2 <- sample(idx2, n *0.7)
  validate_idx2 <- setdiff(idx2, training_idx2)
  training2 <- data2[training_idx2,]
  validation2 <- data2[validate_idx2,]
  
  # 모형분석 1: 로지스틱 분석
  #-----------------
  data_lm_full <- glm(class ~ ., data=training, family=binomial)
  # 로지스틱 평가(상관관계 삭제 )
  y_obs <- validation$class
  yhat_lm <- predict(data_lm_full, newdata = validation, type='response')
  pred_lm <- prediction(yhat_lm, y_obs)
  lm_validation_auc <- performance(pred_lm, "auc")@y.values[[1]]
  #lm_validation_binomial <- binomial_deviance(y_obs, yhat_lm)
  
  data_lm_full2 <- glm(class ~ ., data=training2, family=binomial)
  # 로지스틱 평가2
  y_obs2 <- validation2$class
  yhat_lm2 <- predict(data_lm_full2, newdata = validation2, type='response')
  pred_lm2 <- prediction(yhat_lm2, y_obs2)
  lm_validation_auc2 <- performance(pred_lm2, "auc")@y.values[[1]]
  #lm_validation_binomial2 <- binomial_deviance(y_obs2, yhat_lm2)
  
  if(lm_validation_auc>lm_validation_auc2){
    test_lm <-data_lm_full
  }else{
    test_lm <-data_lm_full2
  }
  y_obs_t<-test_Anal$class
  yhat_lm_t <- predict(test_lm, newdata = test_Anal, type='response')
  pred_lm_t <- prediction(yhat_lm_t, y_obs_t)
  lm_test_auc <- performance(pred_lm, "auc")@y.values[[1]]
  
  #-----------------
  
  # 모형분석 2:랜덤포레스트
  #-----------------
  set.seed(1607)
  data_rf <- randomForest(class ~ ., data=training)
  yhat_rf <- predict(data_rf, newdata=validation, type='prob')[,'1']
  pred_rf <- prediction(yhat_rf, y_obs)
  
  rf_validation_auc<-performance(pred_rf, "auc")@y.values[[1]]
  #binomial_deviance(y_obs, yhat_rf)
  
  #랜덤포레스트2
  data_rf2 <- randomForest(class ~ ., data=training2)
  yhat_rf2 <- predict(data_rf, newdata=validation2, type='prob')[,'1']
  pred_rf2 <- prediction(yhat_rf2, y_obs2)
  
  rf_validation_auc2<-performance(pred_rf2, "auc")@y.values[[1]]
  #binomial_deviance(y_obs2, yhat_rf2)
  
  #랜덤포레스트_test
  if(rf_validation_auc>rf_validation_auc2){
    test_rf <-data_rf
  }else{
    test_rf <-data_rf2
  }
  y_obs_t<-test_Anal$class
  yhat_rf_t <- predict(data_rf, newdata=test_Anal, type='prob')[,'1']
  pred_rf_t <- prediction(yhat_rf_t, y_obs_t)
  rf_test_auc <- performance(pred_rf_t, "auc")@y.values[[1]]
  
  #결과 수집
  per_result[count_p,]<-c(p,lm_validation_auc,lm_validation_auc2,lm_test_auc,
                          rf_validation_auc,rf_validation_auc2,rf_test_auc)
  count_p<-count_p+1
}
write.csv(per_result,'per_result.csv',quote = F,row.names = F)
