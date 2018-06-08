#make_testdataset
# trainingdate.csv open
testdate<- read.csv('csv/testdate.csv', header = F)
test_date <- testdate$V1

#Train.df 설정 
Test.df <- data.frame(word='class',c='clear')

# KOSPI data 읽기 
kospi.data <- read.csv('csv/KOSPI_data.csv',header = T)
#함수실행 
testdateSet<-merge_news_csv(test_date,Test.df,kospi.data)
testNASet<- deleteNA(testdateSet)
wtest<-testdateSet
w_idx <- which(wtest[1,]=='w')
wtest<-wtest[,-w_idx]

ttest<-tdataset(wtest)

#tmp
data3<-ttest
tmp3 <- as.data.frame(cor(data3[,-1], as.numeric(data3$class)))
tmp3 <- na.omit(tmp3)
tmp3 <- tmp3 %>% rename(cor=V1)
tmp3$var <- rownames(tmp3)
data3_mody <- data3[,tmp3$var]
names(data3_mody)[1] <- 'class'
data3_mody$class <- factor(data3$class)
data3<-data3_mody

test_Anal<-data3

write.csv(test_Anal,'test_Anal.csv',quote = F, row.names = T)
