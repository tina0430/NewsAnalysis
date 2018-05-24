
import re 

# 데코레이터
# 기자이름 저장

def kyunghyang(contents, title):
    contents = contents.split('▶')[0]
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [contents.strip(), title.strip()]

def maeile(contents, title):
    contents = contents.split('[')[0]
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [contents.strip(), title.strip()]

def segye(contents, title):
    sp = re.findall('[.][가-힣]{0,2}[=]?[가-힣]{2,} [가-힣]*기자', contents)
    if len(sp) != 0:
        contents = contents.split(sp[0])[0] + '.'  
    else: 
        contents = contents.split('ⓒ 세상을 보는 눈, 글로벌 미디어')[0]
    
    return [contents.strip(), title.strip()]

def economist(contents, title):
    contents = contents.split('[ⓒ 이코노미스트(')[0]
    contents = contents.split('※ 필자는')[0]
    
    email = re.findall(r'([-_\.0-9a-zA-Z]*@joongang\.co\.kr)', contents)
    if len(email) != 0:
        contents = contents.split(email[0])[0]
    
    end = re.findall('※?[가-힣a-zA-Z0-9 ()=]+$', contents)
    if len(end) != 0:
        contents = contents.replace(end[0], '')
    return [contents.strip(), title.strip()]

def han_gyeong(contents, title):
    for i in ('[국고처', '[인사]'):
        if title.rfind(i) != -1:
            contents = ''
    contents = contents.split('(위의 AI인공지능 점수는 재무 데이터를 기반으로 전체 상장 종목과 비교')[0]
    contents = contents.split('자세한 내용은 한국경제TV 다시보기를 통해 볼 수 있습니다.')[0]
    contents = contents.split('ⓒ 한국경제TV')[0]
    
    email = re.findall(r'([-_\.0-9a-zA-Z]*@wowtv\.co\.kr)', contents)
    if len(email) != 0:
        contents = contents.split(email[0])[0]
    
    end = re.findall('[가-힣]+[ ]*기자+[ ]*$', contents)
    if len(end) != 0:
        contents = contents.replace(end[0], '')
    
    end = re.findall('[가-힣]+[ ]*PD+[ ]*$', contents)
    if len(end) != 0:
        contents = contents.replace(end[0], '')
        
    for i in ['디지털 뉴스부', '디지털뉴스부', '라이온봇기자']:
        contents = contents.replace(i, '')
    return [contents.strip(), title.strip()]

#만족
def sbsNews(contents, title):
    contents = contents.split('※ ⓒ SBS & SBS Digital News Lab. : 무단복제 및 재배포 금지')[0]
    contents = contents.split('(영상취재 :')[0]
    contents = contents.split('(영상편집 :')[0]
    contents = contents.split('(사진=')[0]
    
    for i in ['<기자>', '<앵커>']:
        contents = contents.replace(i, '')
    
#     email = re.findall(r'([-_\.0-9a-zA-Z]*@wowtv\.co\.kr)', contents)
    email = re.findall(r'[가-힣 ]{2,}기자\(', contents)
    if len(email) != 0:
        contents = contents.split(email[0])[0]
    return [contents.strip(), title.strip()]

#일요일 다시 긁어야함
def gukmin(contents, title):
    contents = contents.split('뉴시스GoodNews paper ⓒ, 무단전재 및 재배포금지')[0]
    contents = contents.split('GoodNews paper ⓒ, 무단전재 및 재배포금지')[0]
    contents = contents.split('각 부 종합,')[0]
    
    writer = re.findall('[가-힣]+=[가-힣]+', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[0]
    
    writer = re.findall('[가-힣 ]+기자', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[0]
    
    return [contents.strip(), title.strip()]

#[주목! 경매물건]
#허주열 기자
#사진. 아디다스강인귀 기자
#사건번호 17-4368EH경매연구소
#http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=417&aid=0000287606
#대책 마련 시급
#다시 해야함
def moneys(contents, title):
#     contents = contents.split('사건번호')[0]
     
    writer = re.findall(r'\.[가-힣  ]{2,5}기자', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[len(writer)-1]
        
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

def sindonga(contents, title):
    writer_email = re.findall(r'[\| ]*[0-9가-힣  ]+기자[ ]*[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', contents)
    if len(writer_email) != 0:
        contents = contents.split(writer_email[0])[0]
        
    email = re.findall(r'[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', contents)
    if len(email) != 0:
        contents = contents.split(email[0])[0]

    contents = contents.replace('[신동아]', '')
    writer = re.findall('[\| ]*[0-9가-힣  ]+\|', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[len(writer)-1]
        
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

#만족
def chosunbiz(contents, title):
    writer = re.findall(r'\[[가-힣0-9A-Za-z@\. =]*\]chosunbiz.com', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[len(writer)-1]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [contents.strip(), title.strip()]

#얘네는 못거름
#김기찬 고용노동선임기자▶모바일에서 만나는 중앙일보ⓒ중앙일보and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지
#김진상 앰플러스파트너스(주) 대표이사·인하대 겸임교수 jkim@ampluspartners.com
#신성진 배나채 대표 truth64@hanmail.net▶ 중앙일보/친구추가▶ 이슈를 쉽게 정리해주는ⓒ중앙일보, 무단 전재 및 재배포 금지
def joongang(contents, title):
    if title.rfind('[인사]') != -1:
        contents = ''
    
    writer_email = re.findall(r'[가-힣  ]+[0-9A-Za-z\.]+@joongang.co.kr▶', contents)
    if len(writer_email) != 0:
        print(writer_email)
        contents = contents.split(writer_email[0])[len(writer_email)-1]
        
    writer = re.findall(r'[가-힣  ][기자]▶', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[len(writer)-1]
    
    contents = contents.split('[ⓒ 조인스랜드 : JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]')[0]
    contents = contents.split('▶모바일에서 만나는 중앙일보ⓒ중앙일보and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지')[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]


#신상순[ⓒ 한국일보(), 무단 전재 및 재배포 금지]
#그럭저럭
def hankook(contents, title):
    writer_email = re.findall(r'[가-힣 = ]+[0-9A-Za-z\.]+@hankookilbo.com\[ⓒ 한국일보', contents)
    if len(writer_email) != 0:
        print(writer_email)
        contents = contents.split(writer_email[0])[0]
    
    writer = re.findall(r'[가-힣 ]+=?[가-힣]{2,5} 기자\[ⓒ 한국일보', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[len(writer)-1]
        
    contents = contents.split('[ⓒ 한국일보(), 무단 전재 및 재배포 금지]')[0]

    return [contents.strip(), title.strip()]

#그럭저럭
#밑에꺼 못거름
#YTN Star 반서연 기자 (uiopkl22@ytnplus.co.kr)[사진제공 = CJ CGV]
#취재기자ㅣ오인석촬영기자ㅣ윤원식영상편집ㅣ오유철자막뉴스 제작ㅣ이하영[저작권자(c) YTN & YTN PLUS 무단전재 및 재배포 금지]
def ytn(contents, title):
    if title.rfind('[자막뉴스]') != -1:
        writer = re.findall(r'[ 가-힣\ㅣ]+\[저작권자(c)', contents)
        if len(writer) != 0:
            contents = contents.split(writer[0])[0]
    
    if contents.rfind('[앵커]') != -1:
        for i in ('[앵커]', '[기자]'):
            contents = contents.replace(i, '')
        writer = re.findall(r'YTN [가-힣]+[\[a-zA-Z0-9@ytn.co.kr\]]*입니다', contents)
        if len(writer) != 0:
            print(writer)
            contents = contents.split(writer[0])[0]
    contents = contents.split('[저작권자(c) YTN & YTN PLUS 무단전재 및 재배포 금지]')[0]
    contents = contents.split('[사진제공 = CJ CGV]')[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]


def newsis(contents, title):
    writer = re.findall(r'\【[ 가-힣]+=뉴시스\】[ 가-힣]+기자[ =]+', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.replace(writer[0], '')
    
    email = re.findall(r'[a-zA-Z0-9]+@newsis.com', contents)
    if len(email) != 0:
        print(email)
        contents = contents.replace(email[0], '')
    
    photo = re.findall(r'\(사진[ =가-힣]+제공\)', contents)
    if len(photo) != 0:
        print(photo)
        contents = contents.split(photo[0])[0]
    
    contents = contents.split('공감언론 뉴시스가 독자 여러분의 소중한 제보를 기다립니다.')[0]
        
    return [contents.strip(), title.strip()]
#[머니투데이 세종=최우영 기자] ~~~ 세종=최우영 기자 young@
#[머니투데이 중기협력팀 이유미 기자] ~~~ 이유미 기자 youme@
#[머니투데이 김훈남 기자] ~~~ 김훈남 기자 hoo13@mt.co.kr
#[머니투데이 장시복 기자] ~~~ 장시복 기자 sibokism@
#[머니투데이 유희석 기자] ~~~ 유희석 기자 heesuk@mt.co.kr
#[머니투데이 강기준 기자] ~~~ 강기준 기자 standard@
#[머니투데이 뉴욕(미국)=송정렬 특파원] ~~~ 뉴욕(미국)=송정렬 특파원 songjr@mt.co.kr
#[머니투데이 신희은 기자] ~~~ 신희은 기자 gorgon@mt.co.kr
#[머니투데이 김건우 기자] ~~~ 김건우 기자 jai@mt.co.kr
#[머니투데이 이원광 기자, 이동우 기자] 이원광 기자 demian@mt.co.kr, 이동우 기자 canelo@
#[머니투데이 영종도(인천)=최석환 기자] ~~~ 영종도(인천)=최석환 기자 neokism@mt.co.kr
#송지유 기자 clio@, 박진영 기자 jyp@, 배영윤 기자 young25@mt.co.kr
#[머니투데이 송지유 기자, 박진영 기자, 배영윤 기자]

def moneyToday(contents, title):
#     [표]
    writer = re.findall(r'\[머니투데이[ 가-힣 \(\)=,?&?]+\]', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '').strip()
        for i in ('[머니투데이', ']'):
            writer[0] = writer[0].replace(i, '').strip()
        writers = writer[0].split(',')
            
        if len(writers) != 0:
            writer[0] = writers[0].strip()
                
        contents = contents.split(writer[0])[0]
        
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

#
#[아시아경제 이광호 기자] ~~~ 세종=이광호 기자 kwang@asiae.co.kr

def asiae(contents, title):
    for i in ('[부고]', '[인사]'): #'아시아경제 오늘의 뉴스'
        if title.rfind(i) != -1:
            contents = ''
    writer = re.findall(r'\[[ 가-힣=\]*아시아경제[ 가-힣=]+\]', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '').strip()
        for i in ('[', '아시아경제 ','아시아경제', ']'):
            writer[0] = writer[0].replace(i, '').strip()
        contents = contents.split(writer[0])[0]
        
    writer = re.findall(r'[ =가-힣]+[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]*', contents)
    
    if len(writer) != 0:
        print(writer)
        contents = contents.replace(writer[0], '').strip()
        
    bot = re.findall('다음은[가-힣0-9 ]+기준 오늘의[ 가-힣\-]+Top10 입니다.', contents)
    if len(bot) != 0:
        print(bot)
        contents = contents.split(bot[0])[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

#만족
def chosun(contents, title):
    contents = contents.split('[][]- Copyrights ⓒ 조선일보 & chosun.com, 무단 전재 및 재배포 금지 -')[0]
    contents = contents.split('[')[0]
  
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

# ※ 저작권자 ⓒ. 무단 전재-재배포 금지
#크롤링시에 따로 가져오는거 만들어야한당
def financialNews(contents, title):
    contents = contents.replace('※ 저작권자 ⓒ. 무단 전재-재배포 금지', '')
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

#[인사]
#조갑천- Copyrights ⓒ 헤럴드경제 & heraldbiz.com, 무단 전재 및 재배포 금지 -
def herald(contents, title):
    if title.rfind('[인사]') != -1:
        contents = ''
    contents = contents.replace('(본 기사는 헤럴드경제로부터 제공받은 기사입니다.)', '')
    #［ [
    writer = re.findall(r'\[헤럴드경제=[ 가-힣]+\]', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '').strip()
        
    writer = re.findall(r'［헤럴드경제=[ 가-힣]+］', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '').strip()
        
    writer_email = re.findall(r'[가-힣]+ 기자/[ a-zA-Z0-9\.]+@[ a-zA-Z0-9\.]*- Copyrights', contents)
    if len(writer_email) != 0:
        contents = contents.split(writer_email[0])[0]
    
    email = re.findall(r'[a-zA-Z0-9\.]+@[ a-zA-Z0-9\.]*- Copyrights', contents)
    if len(email) != 0:
        contents = contents.split(email[0])[0]
    
    contents = contents.split('- Copyrights ⓒ 헤럴드경제')[0]
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]

    return [contents.strip(), title.strip()]

#프놈펜=김성규 기자 sunggyu@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#세종=김준일 기자 jikim@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#[동아일보] 황태호 기자 taeho@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#동아닷컴 이은정 기자 ejlee@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#서형석 기자 skytree08@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#ⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#김진영 연세대 의대 의학교육학과 교수 kimjin@yuhs.ac·정리=이미영 기자 mylee03@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
def donga(contents, title):
    writer = re.findall('[ 가-힣=]+[a-zA-Z0-9\.]+@donga.com', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[0]
        
    contents = contents.replace('[동아일보]', '')
    contents = contents.replace('ⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지', '')

    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]

    return [contents.strip(), title.strip()]

#방승배·이관범·김윤림 기자 bsb@munhwa.com[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]
#박민철·김성훈 기자 mindom@munhwa.com[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]
#김윤림 기자 bestman@[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]
def munhwa(contents, title):
    writer = re.findall('[ 가-힣=·]+[a-zA-Z0-9\.]+@', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[0]
    contents = contents.replace("[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]", '')

    return [contents.strip(), title.strip()]
    
#(종합)
#[부고][인사]
#(영종도=연합뉴스) 이지은 기자 = ~~~ jieunlee@yna.co.kr
#(서울=연합뉴스) 이태수 기자 = ~~~ tsl@yna.co.kr
#(서울=연합뉴스) 박의래 기자 = ~~~ laecorp@yna.co.kr
#※ 자료 :
def yna(contents, title):
    for i in ('[부고]', '[인사]'):
        if title.rfind(i) != -1:
            contents = ''
    title = title.replace('(종합)', '')
    contents = contents.split('※ 자료 :')[0]
    
    writer = re.findall(r'\([가-힣]+=연합뉴스\)[ 가-힣]+기자 =', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '')
        
    location = re.findall(r'\([가-힣]+=연합뉴스\)', contents)
    if len(location) != 0:
        contents = contents.replace(location[0], '')
    
    email = re.findall(r'[a-zA-Z0-9\.]+@yna.co.kr', contents)  
    if len(email) != 0:
        print(email)
        contents = contents.replace(email[0], '')  
    
    return [contents.strip(), title.strip()]


#[인사]
#▶▶박지환(pjh@joseilbo.com)저작권자 ⓒ 조세일보(http://www.joseilbo.com). 무단전재 및 재배포 금지
def jose(contents, title):
    for i in ('[부고]', '[인사]'):
        if title.rfind(i) != -1:
            contents = ''
    contents = contents.split('▶▶')[0]
    contents = contents.split('저작권자 ⓒ 조세일보(http://www.joseilbo.com). 무단전재 및 재배포 금지')[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]
    
#[한겨레] ~~~ 이정국 기자 jglee@hani.co.kr▶ 한겨레 절친이 되어 주세요![ⓒ한겨레신문 : 무단전재 및 재배포 금지]
#▶ 한겨레 절친이 되어 주세요![ⓒ한겨레신문 : 무단전재 및 재배포 금지]
def hani(contents, title):
    for i in ('[부고]', '[인사]'):
        if title.rfind(i) != -1:
            contents = ''
            
    writer = re.findall(r'[ 가-힣]+[a-zA-Z0-9\.]+@hani.co.kr▶', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[0]
    contents = contents.split('▶ 한겨레 절친이 되어 주세요')[0]
    contents = contents.replace('[한겨레]', '')
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]
#[날씨]~~~[뉴스투데이][정오뉴스]~~~이창민 캐스터[저작권자(c) MBC (http://imnews.imbc.com) 무단복제-재배포 금지]Copyright(c) Since 1996,&All rights reserved.
#김재경 기자 (samana80@naver.com)[저작권자(c) MBC (http://imnews.imbc.com) 무단복제-재배포 금지]Copyright(c) Since 1996,&All rights reserved.
#◀ 앵커 ▶◀ 캐스터 ▶◀ 리포트 ▶

def mbcNews(contents, title):
    remove = ['◀ 앵커 ▶','◀ 캐스터 ▶','◀ 리포트 ▶','[뉴스데스크]','[뉴스투데이]','[뉴스콘서트]', '[정오뉴스]', '[이브닝뉴스]', '▶ ', 
              '날씨였습니다.', '지금까지 스마트리빙이었습니다.', '지금까지 스마트 리빙이었습니다.', '지금까지 스마트리빙플러스였습니다.']
    for i in remove:
        contents = contents.replace(i, '')
    
    announcer = re.findall('[ 가-힣]*MBC뉴스 [가-힣]+입니다.', contents)
    if len(announcer) != 0:
        print(announcer)
        contents = contents.split(announcer[0])[0]
        
    writer = re.findall(r'[ 가-힣/]+\[저작권자\(c\)', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[0]
        
    writer_email = re.findall(r'[ 가-힣]+[\(a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]+\[저작권자\(c\)', contents)
    if len(writer_email) != 0:
        contents = contents.split(writer_email[0])[0]
    
    contents = contents.split('[저작권자(c) MBC')[0]    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [contents.strip(), title.strip()]

#KB금융지주 제공//
#김민수기자 min/김민수
def digitalTimes(contents, title):
    for i in ('[부고]', '[인사]'):
        if title.rfind(i) != -1:
            contents = ''
    
    writer = re.findall(r'\[디지털타임스[ 가-힣]+\]', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.replace(writer[0], '').strip()
        
    writer_email = re.findall(r'[ =가-힣]*기자 [a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]*[/]+[가-힣]+', contents)
    if len(writer_email) != 0:
        print(writer_email)
        contents = contents.split(writer_email[0])[0]

    email = re.findall(r'[a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]*[/]+[가-힣]+', contents)
    if len(email) != 0:
        print(email)
        contents = contents.split(email[0])[0]

    contents = contents.split('/인터넷 마케팅팀')[0]
    return [contents.strip(), title.strip()]

#contents [서울경제][서울경제TV] [앵커][기자][인터뷰]
#/정창신기자 csjung@sedaily.com[영상편집 김지현]저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#/세종=임진혁기자 liberal@sedaily.com저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#/권욱기자저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#/김우보·김상훈기자 ubo@sedaily.com저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
def seoule(contents, title):
    #title 수정 좀더 고민하기 특히 한문
    remove = ['[서울경제]', '[서울경제TV]', '[투데이포커스]', '[표]', '[S머니]', '[이슈&워치]','[금주의 분양캘린더]']
    for i in remove:
        contents = contents.replace(i, '')
    remove = ['[서울경제]', '[서울경제TV]', '[서울경제 디센터]', '[앵커]', '[기자]', '[인터뷰]']
    for i in remove:
        contents = contents.replace(i, '')
    
    contents = contents.split('[이 기사는 증시분석 전문기자 서경뉴스봇(newsbot@sedaily.com)이 실시간으로 작성했습니다.]')[0]
        
    writer = re.findall(r'/[ 가-힣=·]+[a-zA-Z0-9\._@]*저작권자', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[0]
    
    contents = contents.split('[사진=')[0]
    contents = contents.split('저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지')[0]
    
    title.split('오늘의 증시 메모')
    if len(title) != 0:
        title = '오늘의 증시 메모'
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [contents.strip(), title.strip()]
    
def ytnTV(contents, title):
    for i in ('[기자]' ,'[앵커]', '[비즈&]', '[특별기획]', '[기업기상도]'):
        contents = contents.replace(i, '')
    announcer = re.findall('[ 가-힣]*연합뉴스TV [가-힣]+입니다.', contents)
    if len(announcer) != 0:
        print(announcer)
        contents = contents.split(announcer[0])[0]
        
    contents = contents.split('연합뉴스TV : 02')[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [contents.strip(), title.strip()]
    
refin_funcs = {'경향신문' : kyunghyang,
               '매일경제' : maeile,
               '세계일보' : segye,
               '이코노미스트' : economist,
               '중앙SUNDAY' : lambda x, y: x+y,   #제외
               '한국경제TV' : han_gyeong,
               'SBS 뉴스' : sbsNews,
               '국민일보' : gukmin,
               '머니S' : moneys,
               '신동아' : sindonga,
               '조선비즈' : chosunbiz,
               '중앙일보' : joongang,
               '한국일보' : hankook,
               'YTN' : ytn,
               '뉴시스' : newsis,
               '머니투데이' : moneyToday,
               '아시아경제' : asiae,
               '조선일보' : chosun,
               '파이낸셜뉴스' : financialNews,
               '헤럴드경제' : herald,
               '동아일보' : donga,
               '문화일보' : munhwa,
               '연합뉴스' : yna,
               '조세일보' : jose,
               '한겨레' : hani,
               'MBC 뉴스' : mbcNews,
               '디지털타임스' : digitalTimes,
               '서울경제' : seoule,
               '연합뉴스TV' : ytnTV,
               '주간경향' : lambda x, y: x+y,
               '한경비즈니스' : lambda x, y: x+y,
               'MBN' : lambda x, y: x+y,
               '매경이코노미' : lambda x, y: x+y,
               '서울신문' : lambda x, y: x+y,
               '이데일리' : lambda x, y: x+y,
               '주간동아' : lambda x, y: x+y,
               '한국경제' : lambda x, y: x+y,
               'SBS CNBC' : lambda x, y: x+y
               }