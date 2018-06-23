NewsAnalysis
=============
<!--Analyze the stock price using articles written in Korean.<br>
You must have an article json file that is already crawled.<br>
The json file's format is <br>-->

한글로 쓰여진 금융 관련 기사의 형태소 분석을 통해 주가의 등락을 예측하는 프로그램입니다. <br>
금융 관련 기사는 json 파일로 미리 준비되어있어야 하며 그 포멧은 다음과 같습니다. <br>

    {
        "news1" : {"title":"new title", "contents":"new contents", "press":"press name"}, 
        "news2" : {"title":"new title", "contents":"new contents", "press":"press name"}, 
        "news3" : {"title":"new title", "contents":"new contents", "press":"press name"}, 
            . 
            . 
            . 
    }

<br>
Install
-------------
numpy, pandas, jpype, konlpy, customized_konlpy, xlrd 패키지 설치 및 작동이 되어야 합니다.<br>

<br>
KOSPI Crawler
-------------
　코스피 대비값 크롤링 [kospi.py](https://github.com/tina0430/NewsAnalysis/tree/master/kospiCrwaling) <br>
　크롤링 장소 : <https://kr.investing.com/><br>

<br>
Refine
-------------
1. 기사 작성자, 광고, 언론사 이름, 저작권 표시 제거 [refining.py](https://github.com/tina0430/NewsAnalysis/tree/master/newsRefining)
2. 축약어, 영어 단어 리코딩 [recoding.py](https://github.com/tina0430/NewsAnalysis/tree/master/newsRecoding)
3. 형태소 분석 [knlp.py](https://github.com/tina0430/NewsAnalysis/tree/master/nlp)
4. 명사 빈도수 계산 [count.py](https://github.com/tina0430/NewsAnalysis/tree/master/nlp)
5. 불필요한 명사 제거 [filter.py](https://github.com/tina0430/NewsAnalysis/tree/master/nlp)<br>

　1~5를 한 번에 수행 [main.py](https://github.com/tina0430/NewsAnalysis/tree/master/main)

<br>
Analysis
-------------
1. 90일 부터 365일치의 뉴스 단어 빈도수 셋을 각각 만듦
2. 코스피의 대비와 명사 빈도수와의 상관관계 분석(90~365일 치의 단어셋 각각)
3. 상관관계가 0.1 이하인 단어 제거 
4. 학습용 단어와 예측용 단어를 구분(학습용 - 70% 예측용 - 30%)
5. 남은 단어를 가지고 랜덤 포레스트 모형에 넣어보고 회귀분석을 실시 - 최적의 기간을 찾음(1년)
