NewsAnalysis
=============
Analyze the stock price using articles written in Korean.<br>
You must have an article json file that is already crawled.<br>
The json file's format is <br>
{<br>
&nbsp  "news1" : {"title":"new title", "contents":"new contents", "press":"press name"}, <br>
&nbsp  "news2" : {"title":"new title", "contents":"new contents", "press":"press name"}, <br>
&nbsp  "news3" : {"title":"new title", "contents":"new contents", "press":"press name"}, <br>
&nbsp&nbsp .
&nbsp&nbsp .
&nbsp&nbsp .
}<br>

Install
-------------


Crawler
-------------
##KOSPI
from investing.com

Refine
-------------
Analysis
-------------


1. 코스피 지수 크롤링


1. 코스피 지수를 크롤링
2. 이미 크롤링되어있는 뉴스 데이터를 정제
3. 형태소 분석을 통해 명사 추출을 후 명사 빈도수 추출
4. 90일 부터 365일치의 뉴스 단어 빈도수 셋을 각각 만듦
5. 코스피의 대비와 명사 빈도수와의 상관관계 분석(90~365일 치의 단어셋 각각)
6. 상관관계가 0.1 이하인 단어 제거 
7. 학습용 단어와 예측용 단어를 구분(학습용 - 70% 예측용 - 30%)
8. 남은 단어를 가지고 랜덤 포레스트 모형에 넣어보고 회귀분석을 실시 - 최적의 기간을 찾음(1년)
