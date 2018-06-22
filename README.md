NewsAnalysis
=============
Analyze the stock price using articles written in Korean.<br>
You must have an article json file that is already crawled.<br>
The json file's format is <br>

    {
        "news1" : {"title":"new title", "contents":"new contents", "press":"press name"}, 
        "news2" : {"title":"new title", "contents":"new contents", "press":"press name"}, 
        "news3" : {"title":"new title", "contents":"new contents", "press":"press name"}, 
            . 
            . 
            . 
    }

Install
-------------


Crawler
-------------
## KOSPI
<https://kr.investing.com/>

Refine
-------------
1. 기사 작성자, 광고, 언론사 이름, 저작권 표시 제거
2. 축약어, 영어 단어 리코딩
3. 명사만  추출
4. 불필요한 명사 제거

Analysis
-------------
1. 90일 부터 365일치의 뉴스 단어 빈도수 셋을 각각 만듦
2. 코스피의 대비와 명사 빈도수와의 상관관계 분석(90~365일 치의 단어셋 각각)
3. 상관관계가 0.1 이하인 단어 제거 
4. 학습용 단어와 예측용 단어를 구분(학습용 - 70% 예측용 - 30%)
5. 남은 단어를 가지고 랜덤 포레스트 모형에 넣어보고 회귀분석을 실시 - 최적의 기간을 찾음(1년)
