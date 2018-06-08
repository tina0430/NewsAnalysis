# 사용 패키지 
library(stringr)
library(dplyr)
library(ggplot2)
library(MASS)
library(glmnet)
library(randomForest)
library(gbm)
library(rpart)
library(boot)
library(data.table)
library(ROCR)
library(gridExtra)


#확정 함수들 
#01. merge news_csv: make dataset 50개 미만 삭제 
merge_news_csv<- function(f_date,word.df,kospi.data){
  len<-length(f_date)
  count_no<-1
  for (i in c(1:len)){
    #file open
    filename=paste('news_csv/news_',as.character(f_date[i]),'_result.csv')
    filename=str_replace_all(filename,' ','')
    openfile<-read.csv(filename,sep=',',header = T,encoding='CP949')
    
    #delete words _under 50
    wordfile <- subset(openfile, openfile$count>=50)
    
    #change columns names
    names(wordfile)<-c('word',f_date[i])
    
    # merge
    word.df<-merge(word.df,wordfile,by='word',all = T)
    
    #class 
    kdate <- paste(substr(f_date[i],1,4),'-',substr(f_date[i],5,6),'-',substr(f_date[i],7,8))
    kdate <- str_replace_all(kdate,' ','')
    if(kdate %in% kospi.data$date){
      kclass<- kospi.data$against[kospi.data$date==kdate]
      klogic<-ifelse(kclass>=0,1,0)
    }else{
      klogic<-'w'
    }
    
    if (i==1){
      word.df<-subset(word.df, select=-c)
    }
    class_col<-length(word.df)
    word.df[1,c(class_col)]<-klogic
    
    #NA -> 0
    #word.df[is.na(word.df)] <- 0
    
    
    cat('NO:',count_no,'date:',f_date[i],'\n')
    count_no<-count_no+1
  }
  return(word.df)
}

#02. dataset 추출 , NA 5% 이하만 추출 
subset_merge<-function(date_e){
  Tcol<-colnames(TrainingSet)
  enddate<-which(Tcol==date_e)
  startdate<-enddate-p
  dataSet<-TrainingSet[,c(1,c(startdate:enddate))]
  
  #step2: NA %로 삭제
  count_row<-nrow(dataSet)
  count_col<-length(dataSet)-1
  checkNA <- data.frame(word=dataSet$word ,per_NA=c(0))
  print('start_delete NA ')
  for (r in c(2:count_row)){
    percentNA<-sum(dataSet[r,]==0)/count_col 
    checkNA[r,2]<-percentNA
   
  }
  
  checkNA_5 <- subset(checkNA,checkNA$per_NA<=0.05)
  
  #checkNA_5 단어 삭제 
  dataSet <-subset(dataSet,dataSet$word %in% checkNA_5$word) 
  
  return(dataSet)
}

#03.연휴 삭제 
WeekendDelete<-function(wtestset){
  w_len<-sum(wtestset[1,]=='w')-1
  
  for(w in c(1:w_len)) {
    w_idx <- which(wtestset[1,]=='w')
    ifelse(w_idx[1]==2,wcol<-w_idx[2],wcol<-w_idx[1])
    change_col_N <- wcol-1
    sumtest <- c()
    testnrow <- nrow(wtestset)
    for(r in c(2:testnrow)){
      tsum <-sum( as.numeric(wtestset[r,change_col_N]),as.numeric(wtestset[r,wcol]) )
      sumtest <- c(sumtest,tsum)
    }
    #sum w 
    wtestset[,change_col_N]<-c(wtestset[1,change_col_N],sumtest)
    #delete W
    
    wtestset<-subset(wtestset, select = -wcol)
    cat('delete_col_No.:',wcol,'date :',names(wtestset[wcol]),'\n')
  }
  
  if(wtestset[1,2]=='w'){wtestset<-wtestset[,-2]}else{print('ok')}
  
  return(wtestset)
}

#04.행렬치환
tdataset<-function(wtestset){
  rownames(wtestset)<- wtestset$word
  wtestset<-wtestset[,-1]
  wtestset<-t(wtestset)
  wtestset<-data.frame(wtestset)
  return(wtestset)
}

#NA 5%미만  삭제
deleteNA<-function(dataSet){
  count_row<-nrow(dataSet)
  count_col<-length(dataSet)-1
  checkNA <- data.frame(word=dataSet$word ,per_NA=c(0))
  for (r in c(2:count_row)){
    percentNA<-sum(dataSet[r,]==0)/count_col 
    checkNA[r,2]<-percentNA
    cat(r,'  ')
  }
  
  checkNA_5 <- subset(checkNA,checkNA$per_NA<=0.05)
  
  #checkNA_5 단어 삭제 
  dataSet <-subset(dataSet,dataSet$word %in% checkNA_5$word)
  
  return(dataSet)
}

#05.binomial_deviance
binomial_deviance <- function(y_obs, yhat){
  epsilon = 0.0001
  yhat = ifelse(yhat < epsilon, epsilon, yhat)
  yhat = ifelse(yhat > 1-epsilon, 1-epsilon, yhat)
  a = ifelse(y_obs==0, 0, y_obs * log(y_obs/yhat))
  b = ifelse(y_obs==1, 0, (1-y_obs) * log((1-y_obs)/(1-yhat)))
  return(2*sum(a + b))
}
