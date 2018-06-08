
# trainingdate.csv open
trainingdate<- read.csv('csv/trainingdate.csv', header = F)
f_date <- trainingdate$V1

#Train.df 설정 
Train.df <- data.frame(word='class',c='clear')
#Wordset 설정
WordSet <- data.frame(word='class',c='clear')
#NA_Set 설정 
NA_Set<-data.frame()
# KOSPI data 읽기 
kospi.data <- read.csv('csv/KOSPI_data.csv',header = T)

#make dataset 50개 미만 삭제 
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
    word.df[is.na(word.df)] <- 0
    
    
    cat('NO:',count_no,'date:',f_date[i],'\n')
    count_no<-count_no+1
  }
  return(word.df)
}

TrainingSet<-merge_news_csv(f_date,Train.df,kospi.data)
write.csv(TrainingSet,'TrainingSet2.csv',quote = F,row.names = F)



#NA_Set에 추가
#if(i==1){
#  Na_set[i]<-word.df$word
#}else{
#  count_row<-nrow(word.df)
#  len<-length(word.df)-1
#  checkNA <- data.frame(word=Analdataset_all$word ,per_NA=c(0))
#  for (r in c(2:count_row)){
#    percentNA<-sum(Analdataset_all[r,]==0)/len 
#    checkNA[r,2]<-percentNA
#  }
#  NA_Set[i]<- checkNA$word[checkNA$per_NA<=0.05]
#}