numpy, pandas, jpype, konlpy 패키지 설치 및 작동이 되어야 합니다.<br/>
xlrd 패키지 설치가 필요합니다.</br>
<br/>
konlp<br/>
settings.csv<br/>
news_folder:뉴스 폴더의 경로<br/>
filter_dictionary:필터링 사전 xlsx파일의 경로<br/>
konlp_engine:사용할 형태소 분석 엔진의 클래스 이름<br/>
konlp_function:사용할 형태소 분석 함수 이름<br/>
result_folder:결과 csv가 저장될 폴더의 경로<br/>
<br/>
settings.csv 변경 후 main.py를 실행.<br/>
<br/>
crawling<br/>
kospi.py<br/>
코드의 start 부터 end 까지의 코스피 데이터를 크롤링<br/>
날짜 형식 : YYYY/MM/DD<br/>
