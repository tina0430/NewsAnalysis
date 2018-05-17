from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter
from konlpy.tag import Hannanum

from collections import Counter

import time
import json

class NLPObject:
    def __init__(self):
        pass
    pass

news1 = '''
[fn 오후시황]코스피 개인 및 외국인 매도에 2470선으로 밀려

코스피가 개인 및 외국인 매도에 2470선으로 밀렸다. 

코스피는 14일 오후 1시 40분 전거래일 대비 3.46포인트(0.14%) 내린 2474.25에 거래되고 있다. 

이날 코스피는 전 거래일 대비 5.26포인트(0.21%) 오른 2482.97에 개장했다. 

기관은 1133억원을 순매수했다. 하지만 개인과 외국인이 각각 701억원, 563억원을 순매도하며 지수를 끌어내렸다. 

규모별로 대형주(-0.44%)는 하락세다. 반면 중형주(1.46%), 소형주(1.03%)는 상승세다. 업종별로 철강 및 금속(3.42%), 기계(1.35%), 비금속광물(9.13%) 등이 상승세다. 반면 전기 전자(-1.78%), 의약품(-1.87%)은 하락세다. 

시가총액 상위종목별로 삼성전자(-2.53%), SK하이닉스(-1.05%), 삼성물산(-1.54%) 등은 하락세다. 반면 포스코(3.21%), LG화학(2.17%) 등은 상승세다. 

코스닥은 전거래일 대비 4.78포인트(0.55%) 내린 861.15에 거래되고 있다. 

ggg@fnnews.com 강구귀 기자 
'''

news2 = '''
남북경협주 잔치에 소외된 삼성전자…'공매도 급증'

[머니투데이 김주현 기자] [[내일의전략] 외국인 하루동안 삼성전자 211만주 순매도…장 중 한때 5만원선 아래로 ]

삼성전자가 5만원선을 위협받고 있다. 남북한 평화 분위기에 남북경협주가 폭발적인 거래량과 주가 상승률을 기록하는 가운데 IT주 소외 현상이 심화되고 있다. 

삼성전자는 14일 2.34%(1200원) 하락한 5만100원에 거래를 마쳤다. 장 중 한때 4만9900원까지 하락했다. 이날 외국인은 211만주(1058억원 어치), 기관은 99만주(497억원 어치)를 순매도했다. 개인은 313만주(1570억원 어치) 순매수했다. 


공매도 전문 금융정보업체 트루쇼트에 따르면 전 거래일(11일) 삼성전자에는 264만주의 공매도가 몰려 공매도 비중이 25%를 넘었다. 공매도 거래대금은 1367억원을 기록했다. 

삼성전자 공매도 비중이 20%를 넘은 건 지난해 3월13일(26.4%) 이후 약 1년여 만이다. 대차 잔고량은 액면분할 첫날인 지난 4일 4602만6975주에서 지난 11일 1억1254만8089주로 급증했다. 이에 따른 대차잔고 비중도 1.23%에서 3.01%로 증가했다. 대차잔고는 투자자들이 주식을 빌린 뒤 갚지 않은 물량이다. 

공매도는 주가 하락이 예상될 때 시세 차익을 얻는 투자 전략이다. 주식을 빌려 미리 판 다음, 실제 주가가 하락하면 팔았던 가격보다 싼 값에 주식을 사들여 갚는 식이다. 공매도가 급증했다는 건 11일 종가인 5만1300원보다 주가가 하락할 것으로 예상한 투자자가 많다는 의미다. 

반도체 업황 호조와 시장 기대치를 웃돈 1분기 실적 발표에도 삼성전자는 지지부진한 흐름을 이어가고 있다. 시장 관심이 남북경협주에 쏠리면서 액면분할 이후 개인투자자의 거래량 증가가 기대에 미치지 못해서다. 

남북정상회담 이후 투자자들의 남북경협주 거래량은 폭발적으로 늘었다. 현대건설 현대로템 등 대표적인 남북경협주 주가도 무서운 기세로 오르고 있다. 현대건설은 이날 주가가 13.82% 급등했고 거래대금 9381억원을 기록했다. 

증시 주도주가 건설을 비롯한 남북경협주로 넘어가면서 일각에선 '대북주가 아니면 주식도 아니다'라는 말까지 나오고 있다. 대표적으로 SK하이닉스와 삼성전기는 실적 전망치가 큰 폭으로 상향했는데도 주가 반응은 미지근하다. 시장이 실적보다 수급에 집중하고 있다는 방증이다. 

송명섭 하이투자증권 연구원은 "최근 삼성전자 주가 약세는 거래 정지 기간 반영되지 못했던 글로벌 IT주들의 주가 하락과 액면분할 전 몰렸던 매수세가 매도로 돌아서면서 나타나는 것"이라고 설명했다. 

이어 "단기적으론 주가가 지지부진한 흐름을 보일 수 있겠고 실적 측면에서는 3분기까지는 양호한 실적을 보이다 4분기부터는 반도체 업황이 꺾일 수 있다"고 지적했다. 

다만 삼성전자는 펀더멘털이 견고하고 배당확대 등 주주친화정책을 앞세우고 있어 장기적으로 주가 상승 여력이 있다는 분석이다. 금융정보업체 와이즈에프앤에 따르면 액면분할 이후 삼성전자 목표가를 새롭게 제시한 5개 증권사의 평균 목표주가는 6만9200원이다. 

김주현 기자 naro@

<저작권자 ⓒ '돈이 보이는 리얼타임 뉴스' 머니투데이, 무단전재 및 재배포 금지>
'''

def write_list(data, fileobj):
    for i, line in enumerate(data):
        fileobj.write(line)
        if i > 0 and i % 5 == 0:
            fileobj.write('\n')
        else:
            fileobj.write('\t')

def write_pos(pos_data, fileobj):
    for i, line in enumerate(pos_data):
        txt = ''
        for j, cell in enumerate(line):
            if j == 0:
                txt = txt + '%s' %cell
            else:
                txt = txt + ':%s'%cell
        
        txt = txt + '\t'
        
        fileobj.write(txt)

        if i > 0 and i % 5 == 0:
            fileobj.write('\n')
#         else:
#             fileobj.write('  ')
        
def run_kkma(data):
    kkma = Kkma()
    start_time = time.time()
    print('kkma 시작')
    kkma_morphs = kkma.morphs(data)
    kkma_nouns = kkma.nouns(data)
    kkma_pos = kkma.pos(data)
    end_time = time.time()
    print('kkma 끝 - %s 초' % str(end_time - start_time) )
    kkma_sentences = kkma.sentences(data)
    
    with open('kkma.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('kkma time : %s s\n' % str(end_time - start_time) )
        fstream.write('kkma_morphs\n')
        write_list(kkma_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_nouns\n')
        write_list(kkma_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_pos\n')
        write_pos(kkma_pos, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_sentences\n')
        write_list(kkma_sentences, fstream)
        fstream.write('\n')

def run_komoran(data):
    komoran = Komoran()
    start_time = time.time()
    print('komoran 시작')
    komoran_morphs = komoran.morphs(data)
    komoran_nouns = komoran.nouns(data)
    komoran_pos = komoran.pos(data)
    end_time = time.time()
    print('komoran 끝 - %s 초' % str(end_time - start_time) )
    
    
    with open('komoran.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('komoran time : %s s\n' % str(end_time - start_time) )
        fstream.write('komoran_morphs\n')
        write_list(komoran_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('komoran_nouns\n')
        write_list(komoran_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('komoran_pos\n')
        write_pos(komoran_pos, fstream)
        fstream.write('\n')
    
def  run_twitter(data, bMorphs = False, bNouns = False, bPos = False):
    twitter = Twitter()
    start_time = time.time()
    nlp_func = []
    write_func = []
    titles = []
    if bMorphs:
        titles.append('twitter' + '_morphs\n')
        nlp_func.append(twitter.morphs)
        write_func.append(write_list)
    if bNouns:
        titles.append('twitter' + '_nouns\n')
        nlp_func.append(twitter.nouns)
        write_func.append(write_list)
    if bPos:
        titles.append('twitter' + '_pos\n')
        nlp_func.append(twitter.pos)
        write_func.append(write_pos)
        
    nlp_results = []
    print('twitter 시작')
    for i in range(len(titles)):
        nlp_results.append(nlp_func[i](data))
        
#     twitter_morphs = twitter.morphs(data)
#     twitter_nouns = twitter.nouns(data)
#     twitter_pos = twitter.pos(data)
    end_time = time.time()
    print('twitter 끝 - %s 초' % str(end_time - start_time) )
    
    with open('twitter.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('twitter time : %s s\n' % str(end_time - start_time) )
#         fstream.write('twitter_morphs\n')
#         write_list(twitter_morphs, fstream)
#         fstream.write('\n\n')
#         
#         fstream.write('twitter_nouns\n')
#         write_list(twitter_nouns, fstream)
#         fstream.write('\n\n')
#         
#         fstream.write('twitter_pos\n')
#         write_pos(twitter_pos, fstream)
#         fstream.write('\n')
        for i in range(len(titles)):
            fstream.write(titles[i])
            write_func[i](nlp_results[i], fstream)
            

def run_hannanum(data):
    hannanum = Hannanum()
    start_time = time.time()
    print('hannanum 시작')
    hannanum_morphs = hannanum.morphs(data)
    hannanum_nouns = hannanum.nouns(data)
    hannanum_pos = hannanum.pos(data)
    end_time = time.time()
    print('hannanum 끝 - %s 초' % str(end_time - start_time) )
    
    with open('hannanum.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('hannanum time : %s s\n' % str(end_time - start_time) )
        fstream.write('hannanum_morphs\n')
        write_list(hannanum_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('hannanum_nouns\n')
        write_list(hannanum_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('hannanum_pos\n')
        write_pos(hannanum_pos, fstream)
        fstream.write('\n')
        


if __name__ == '__main__':
    news_route = r'C:\Users\acorn\Downloads\news20180323.json'
    with open(news_route, 'r', encoding='utf-8') as f:
        jdata = json.load(f)
        cnt = len(jdata)
        news = ''
        for i in range(1, cnt-1):
            news += jdata['news'+str(i+1)]['title'] + ' '
            news += jdata['news'+str(i+1)]['contents'] + ' '
    
    #run_kkma(news)
    #run_komoran(news2)
    #run_hannanum(news2)
    #run_twitter(news2, bNouns = True)
    run_twitter(news, bNouns=True)
