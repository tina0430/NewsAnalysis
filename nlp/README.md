numpy, pandas, jpype, konlpy 패키지 설치 및 작동이 되어야 합니다.<br/>
xlrd 패키지 설치가 필요합니다.</br>
<br/>
konlp<br/>
settings.csv<br/>
news_folder:뉴스 폴더의 경로, 하위 폴더의  모든  news_YYYYMMDD.json 파일을 찾아냅니다.<br/>
result_folder:결과 csv가 저장될 폴더의 경로<br/>
filter_dictionary:필터링 사전 xlsx파일의 경로<br/>
user_dictionary:사용자 사전 csv의 경로<br/>
konlp_engine:사용할 형태소 분석 엔진의 클래스 이름, Twitter 사용자 사전 = cTwitter<br/>
konlp_function:사용할 형태소 분석 함수 이름<br/>
<br/>
settings.csv 변경 후 main.py를 실행.<br/>
settings.csv의 경로는 상대경로와 절대경로 모두를 허용합니다.<br/>
<br/>
