NewsAnalysis
=============
[한국어](README.md) [English](README.en.md) 

Analyze the stock price using articles written in Korean.<br>
You must have an article json file that is already crawled.<br>
The json file's format is.. <br>

    {
        "news1" : {"title":"news title", "contents":"news contents", "press":"press name"}, 
        "news2" : {"title":"news title", "contents":"news contents", "press":"press name"}, 
        "news3" : {"title":"news title", "contents":"newss contents", "press":"press name"}, 
            . 
            . 
            . 
    }

<br>

Install
-------------
You must install numpy, pandas, konlpy, customized_konlpy, xlrd pakage.<br>

<br>

KOSPI Crawler
-------------
　코스피 대비값 크롤링 [kospi.py](https://github.com/tina0430/NewsAnalysis/tree/master/kospiCrawling) <br>
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
