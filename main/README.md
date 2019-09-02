numpy, pandas, konlpy 패키지 설치 및 작동이 되어야 합니다.<br/>
customized_konlpy, xlrd 패키지 설치가 필요합니다.<br/>
<br/>
./files : 설정파일과 뉴스 데이터 경로의 기본값으로 설정되어 있는 디렉토리들이 들어있습니다.<br/>
./files/news_original : settings.csv의 news_folder의 기본값으로 설정되어 있는 경로입니다.<br/>
./files/result : 최종 결과물을 저장하는 경로입니다.<br/>
./files/news_recoding : 201806 - 사용하지 않음<br/>
./files/news_refining : 201806 - 사용하지 않음<br/>
./files/nouns : 201806 - 사용하지 않음<br/>
./files/result_nouns : 201806 - 사용하지 않음<br/>
<br/>
./files/settings.csv<br/>
- news_folder:뉴스 폴더의 경로, 하위 폴더의 모든 news_YYYYMMDD.json 파일을 찾아냅니다.<br/>
- result_folder:결과 csv가 저장될 폴더의 경로<br/>
- filter_dictionary:필터링 사전 xlsx파일의 경로<br/>
- user_dictionary:사용자 사전 csv의 경로<br/>
- konlp_engine:사용할 형태소 분석 엔진의 클래스 이름, Twitter 사용자 사전 = cTwitter<br/>
- konlp_function:사용할 형태소 분석 함수 이름<br/>
<br/>
settings.csv 안의 각 항목에 삽입되는 경로는 상대경로와 절대경로 모두를 허용합니다.<br/>
settings.csv의 경로를 변경할 때, main.py 에서 './files/settings.csv' 를 모두 새로운 경로로 수정해야 합니다.<br/>
<br/>
./main : 모든 로직을 수행하는 main.py 가 들어있는 경로 입니다.<br/>
./files/settings.csv 의 정보를 읽어들이고 이를 기반으로 main.py를 실행합니다. (main() 함수를 실행.)<br/>
main.py 의 main() 안에 모든 로직이 들어있습니다.<br/>
뉴스 읽기 - refine - recoding - 형태소 분석 - 빈도수 계산 - 필터링 - 결과물 저장 순입니다.<br/>
<br/>
main() 이 종료될 때 main 폴더에 간단한 로그 파일을 생성합니다.<br/>
각 뉴스파일 1개를 분석하는데 걸린 실행 시간, 각 로직의 소요 시간을 기록합니다.</br>
201806 - 에러 메세지는 넣지 못했습니다.<br/>
<br/>
데이터의 양이 많을 경우, 메모리 초과로 인한 오류가 발생할 수 있습니다.<br/>
컴퓨터의 메모리에 따라 다르지만 대략 3~6개월 단위로 끊어서 실행하는 것을 권장합니다.<br/>
<br/>
./kospiCrawling : 코스피 크롤링 관련 디렉토리입니다.<br/>
kospi 크롤링은 .\kospiCrawling\kospi.py 를 별개로 실행해야 합니다.<br/>
<br/>
./nlp : 형태소 분석 및 빈도수 계산, 필터링 관련 디렉토리입니다.<br/>
./nlp/count.py : 빈도수 계산<br/>
./nlp/filter.py : 필터링<br/>
./nlp/knlp.py : 형태소 분석<br/>
./nlp/process.py : main.py의 프로토타입, 201806 - 사용하지 않음<br/>
./nlp/twitter_userdict_test.py : cKonlp 테스트 코드, 201806 - 사용하지 않음<br/>
./nlp/settings.csv : ./files/settings.csv 로 옮김. 201806 - 사용하지 않음<br/>
<br/>
./newsRecoding : recoding 관련 디렉토리입니다.<br/>
./newsRecoding/recode.json : recoding 사전이 정의되어 있는 파일입니다.<br/>
./newsRecoding.recoding.py : recoding 을 수행합니다.<br/>
<br/>
./newsRefine : refine 관련 디렉토리입니다.<br/>
./newsRefine/functions.py : 언론사별 데이터 정제 방법 정의
./newsRefine/refining.py : 데이터 정제 