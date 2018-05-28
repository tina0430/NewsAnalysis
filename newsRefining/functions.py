import re 

# 기자이름 저장?
# patterns 순서 대빵 중요

#이종우 IBK투자증권 리서치센터장[ⓒ 이코노미스트() and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]
#김성희 기자 kim.sunghee@joongang.co.kr[ⓒ 이코노미스트() and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]
#남화영 헤럴드경제 스포츠팀 편집장[ⓒ 이코노미스트() and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]
#조원경 기획재정부 국제금융심의관[ⓒ 이코노미스트() and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]
#장중호 경영컨설턴트[ⓒ 이코노미스트() and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]
#※ 필자는 

#일요일 다시 긁어야함 - 국민일보

#[주목! 경매물건]
#허주열 기자
#사진. 아디다스강인귀 기자
#사건번호 17-4368EH경매연구소
#http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=417&aid=0000287606
#대책 마련 시급
#다시 해야함
def moneys(title, contents):
#     contents = contents.split('사건번호')[0]
     
    writer = re.findall(r'\.[가-힣  ]{2,5}기자', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[len(writer)-1]
        
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [title.strip(), contents.strip()]

def sindonga(title, contents):
    (((r'\]', 2),), 
     ((r'[\| ]*[0-9가-힣  ]+기자[ ]*[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', 1),(r'[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', 1),
      (r'\[신동아\]', 0)))
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
    
    return [title.strip(), contents.strip()]

#만족
def chosunbiz(title, contents):
    writer = re.findall(r'\[[가-힣0-9A-Za-z@\. =]*\]chosunbiz.com', contents)
    if len(writer) != 0:
        contents = contents.split(writer[0])[len(writer)-1]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [title.strip(), contents.strip()]

#얘네는 못거름
#김기찬 고용노동선임기자▶모바일에서 만나는 중앙일보ⓒ중앙일보and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지
#김진상 앰플러스파트너스(주) 대표이사·인하대 겸임교수 jkim@ampluspartners.com
#신성진 배나채 대표 truth64@hanmail.net▶ 중앙일보/친구추가▶ 이슈를 쉽게 정리해주는ⓒ중앙일보, 무단 전재 및 재배포 금지
def joongang(title, contents):
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
    
    return [title.strip(), contents.strip()]


#신상순[ⓒ 한국일보(), 무단 전재 및 재배포 금지]
#그럭저럭
def hankook(title, contents):
    writer_email = re.findall(r'[가-힣 = ]+[0-9A-Za-z\.]+@hankookilbo.com\[ⓒ 한국일보', contents)
    if len(writer_email) != 0:
        print(writer_email)
        contents = contents.split(writer_email[0])[0]
    
    writer = re.findall(r'[가-힣 ]+=?[가-힣]{2,5} 기자\[ⓒ 한국일보', contents)
    if len(writer) != 0:
        print(writer)
        contents = contents.split(writer[0])[len(writer)-1]
        
    contents = contents.split('[ⓒ 한국일보(), 무단 전재 및 재배포 금지]')[0]

    return [title.strip(), contents.strip()]

#그럭저럭
#밑에꺼 못거름
#YTN Star 반서연 기자 (uiopkl22@ytnplus.co.kr)[사진제공 = CJ CGV]
#취재기자ㅣ오인석촬영기자ㅣ윤원식영상편집ㅣ오유철자막뉴스 제작ㅣ이하영[저작권자(c) YTN & YTN PLUS 무단전재 및 재배포 금지]
def ytn(title, contents):
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
    
    return [title.strip(), contents.strip()]
def newsis(title, contents):
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
        
    return [title.strip(), contents.strip()]
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
def moneyToday(title, contents):
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
    
    return [title.strip(), contents.strip()]

#
#[아시아경제 이광호 기자] ~~~ 세종=이광호 기자 kwang@asiae.co.kr

def asiae(title, contents):
    
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
    
    return [title.strip(), contents.strip()]

#크롤링시에 따로 가져오는거 만들어야한당 - 파이낸셜


#[인사]
#조갑천- Copyrights ⓒ 헤럴드경제 & heraldbiz.com, 무단 전재 및 재배포 금지 -
def herald(title, contents):
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

    return [title.strip(), contents.strip()]

#프놈펜=김성규 기자 sunggyu@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#세종=김준일 기자 jikim@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#[동아일보] 황태호 기자 taeho@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#동아닷컴 이은정 기자 ejlee@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#서형석 기자 skytree08@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#ⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지
#김진영 연세대 의대 의학교육학과 교수 kimjin@yuhs.ac·정리=이미영 기자 mylee03@donga.comⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지

#방승배·이관범·김윤림 기자 bsb@munhwa.com[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]
#박민철·김성훈 기자 mindom@munhwa.com[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]
#김윤림 기자 bestman@[Copyrightⓒmunhwa.com '대한민국 오후를 여는 유일석간 문화일보' 무단 전재 및 재배포 금지()]
    
#(종합)
#[부고][인사]
#(영종도=연합뉴스) 이지은 기자 = ~~~ jieunlee@yna.co.kr
#(서울=연합뉴스) 이태수 기자 = ~~~ tsl@yna.co.kr
#(서울=연합뉴스) 박의래 기자 = ~~~ laecorp@yna.co.kr
#※ 자료 :
    
#[한겨레] ~~~ 이정국 기자 jglee@hani.co.kr▶ 한겨레 절친이 되어 주세요![ⓒ한겨레신문 : 무단전재 및 재배포 금지]
#▶ 한겨레 절친이 되어 주세요![ⓒ한겨레신문 : 무단전재 및 재배포 금지]

#[날씨]~~~[뉴스투데이][정오뉴스]~~~이창민 캐스터[저작권자(c) MBC (http://imnews.imbc.com) 무단복제-재배포 금지]Copyright(c) Since 1996,&All rights reserved.
#김재경 기자 (samana80@naver.com)[저작권자(c) MBC (http://imnews.imbc.com) 무단복제-재배포 금지]Copyright(c) Since 1996,&All rights reserved.
# ◀ 앵커 ▶◀ 캐스터 ▶◀ 리포트 ▶

#얘네 못거름 - 디지텉 타임즈..?
#KB금융지주 제공//
#김민수기자 min/김민수

#contents [서울경제][서울경제TV] [앵커][기자][인터뷰]
#/정창신기자 csjung@sedaily.com[영상편집 김지현]저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#/세종=임진혁기자 liberal@sedaily.com저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#/권욱기자저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#/김우보·김상훈기자 ubo@sedaily.com저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
#저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지
    
#© 주간경향 (), 무단전재 및 재배포 금지〈경향신문은 한국온라인신문협회(www.kona.or.kr)의 디지털뉴스이용규칙에 따른 저작권을 행사합니다.〉

#[한경비즈니스=김정우 기자] ~~~ enyou@hankyung.com
#[카드뉴스] 글·그래픽 : 한경비즈니스 강애리 기자 (arkang@hankyung.com)
#[오태민 크립토 비트코인 연구소장]
#[한경비즈니스=노민정 한경BP 출판편집자]
#[한경비즈니스=김영은 기자] kye0218@hankyung.com
#[한경비즈니스=박희진 신한금융투자 애널리스트, 2017 하반기 섬유·의복 부문 베스트 애널리스트]
#[아기곰 ‘재테크 불변의 법칙’ 저자]

#[ 이상범 기자 / boomsang@daum.net ]< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#[MBN 온라인뉴스팀]< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#MBN뉴스 차민아입니다.< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#MBN뉴스 김지영입니다. [gutjy@mbn.co.kr]영상편집 : 박찬규< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#MBN 뉴스 이상은입니다.영상취재: 이권열 기자영상편집: 서정혁< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#MBN뉴스 김민수입니다.[ smiledream@mbn.co.kr ]영상취재 : 임채웅 기자영상편집 : 이주호< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#【 앵커멘트 】【 기자 】
#▶ 인터뷰 : 류관중 / 금호타이어 노조 실장- ▶ 스탠딩 : 민지숙 / 기자- ▶ 인터뷰 : 오원만 / 국토부 첨단항공과장- ▶ 인터뷰(☎) : '신과함께-인과 연' 홍보 관계자-
#MBN뉴스 민지숙입니다.영상취재: 김 원 기자영상편집: 김경준< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#MBN뉴스 이동훈입니다. [batgt@naver.com]영상취재 : 조영민 기자영상편집 : 김민지< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >
#[MBN스타=김승진 기자]

#온라인 뉴스팀 기자(sbscnbcnews@sbs.co.kr)
#(자세한 내용은 동영상을 시청하시기 바랍니다.)
#SBSCNBC 이광호입니다.이광호 기자(shinytiger@sbs.co.kr)
#SBSCNBC 장가희입니다.장가희 기자(gani@sbs.co.kr)
#SBSCNBC 이한라입니다.이한라 기자(hlmt@sbs.co.kr)
#이한승 기자(detective@sbs.co.kr)
#이한라 기자였습니다.이한라 기자(hlmt@sbs.co.kr)
#지금까지 SBSCNBC 김성현입니다,김성현 기자(now@sbs.co.kr)
#지금까지 삼성동 코엑스 월드IT쇼 현장에서 SBSCNBC 이시은입니다.이시은 기자(see@sbs.co.kr)
#SBSCNBC 박기완입니다.박기완 기자(sentito@sbs.co.kr)
#한편 해솔산업 차선 분리대에 대한 더욱 자세한 정보는 해솔산업 홈페이지를 통해 확인할 수 있다.온라인 뉴스팀 기자(sbscnbcnews@sbs.co.kr)
#SK엠앤서비스에 대한 자세한 내용은 홈페이지에서 알아볼 수 있으며, 회원가입 후 서비스를 이용할 수 있다.온라인 뉴스팀 기자(sbscnbcnews@sbs.co.kr)
#자세한 사항은 5스타 홈페이지 및 주거래 증권사에서 5스타 서비스를 확인하시고 고객센터로 문의하시기 바랍니다.CNBCbiz팀 기자(kimdh@sbs.co.kr)
#(자세한 내용은 동영상을 시청하시기 바랍니다.)CNBCbiz팀 기자(kimdh@sbs.co.kr)
#지금까지 보도국에서 박세정이었습니다.
#앱 설치 시 생방송 및 이벤트 등의 알림을 받아볼 수 있다.CNBCbiz팀 기자(kimdh@sbs.co.kr)
#우형준 기자 잘 들었습니다.우형준 기자(hyungjun.woo@sbs.co.kr)
#이한라 기자였습니다.이한라 기자(hlmt@sbs.co.kr)
#보다 자세한 사항은 e편한세상 홈페이지에서 확인할 수 있다.온라인 뉴스팀 기자(sbscnbcnews@sbs.co.kr)
#[SBSCNBC 뉴미디어팀](기획 : 손석우 / 구성 : 김미화 / 편집 : 서이경)

patterns= {'경향신문' : (((r'\]', 2),), (('▶', 1),)),
           '매일경제' : (((r'\]', 2),), ((r'\[', 1),)),
           '세계일보' : (((r'\]', 2),), 
                      ((r'[a-zA-Z0-9\._]+@segye.com', 0),('[ =,가-힣]*ⓒ', 1), ('ⓒ 세상을 보는 눈, 글로벌 미디어', 1))),
           '이코노미스트' : (((r'\]', 2),), 
                         ((r'([ 가-힣]*[-_\.0-9a-zA-Z]+@joongang\.co\.kr\[ⓒ 이코노미스트)', 1), 
                          ('※', 1), (r'[ 가-힣a-zA-Z]*\[ⓒ 이코노미스트', 1))),
           '중앙SUNDAY' : (((r'\]', 2),), ((r'@', 1),)),   #제외
           '한국경제TV' : (((r'\[국고처', 3), (r'\[인사\]',3 )), 
                        ((r'\(위의 AI인공지능 점수는 재무 데이터를 기반으로', 1), ('자세한 내용은 한국경제TV 다시보기', 1), ('ⓒ 한국경제TV', 1), 
                         (r'([-_\.0-9a-zA-Z]*@wowtv\.co\.kr\)', 1), ('[가-힣]+[ ]*기자+[ ]*$', 0), ('[가-힣]+[ ]*PD+[ ]*$', 0),
                         ('디지털 뉴스부', 0), ('디지털뉴스부', 0), ('라이온봇기자', 0))),
           'SBS 뉴스' : (((r'\]', 2),), #흠 
                        (('※ ⓒ SBS', 1), (r'\(영상취재 :', 1), (r'\(영상편집 :', 1), (r'\(사진=', 1), ('<기자>', 0), ('<앵커>', 0), 
                         (r'[가-힣 ]{2,}기자\(', 1))),
           '국민일보' : (((r'\]', 2),), #흠 
                      (('뉴시스GoodNews paper ⓒ', 1), ('GoodNews paper ⓒ', 1), ('각 부 종합,', 1), ('[가-힣]+=[가-힣]+', 1), 
                       ('[가-힣 ]+기자', 1))),
           '머니S' : (((r'\]', 2),), (('▶', 1),)),
           '신동아' : (((r'\]', 2),), 
                     ((r'[\| ]*[0-9가-힣  ]+기자[ ]*[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', 1),(r'[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', 1),
                      (r'\[신동아\]', 0))),
           '조선비즈' : (((r'\]', 2),), (('▶', 1),)),
           '중앙일보' : (((r'\]', 2),), (('▶', 1),)),
           '한국일보' : (((r'\]', 2),), (('▶', 1),)),
           'YTN' : (((r'\]', 2),), (('▶', 1),)),
           '뉴시스' : (((r'\]', 2),), (('▶', 1),)),
           '머니투데이' : (((r'\]', 2),), (('▶', 1),)),
           '아시아경제' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\[포토\]', 0), (r'\]', 2)), 
                        ((r'\[[ 가-힣=\]*아시아경제[ 가-힣=]+\]', 0), (r'\[', 1), ('아시아경제 ', 1), (']', 1), 
                         (r'[ 가-힣 =]+[a-zA-Z0-9\._]@asiae.co.kr', 1))),
           '조선일보' : (((r'\]', 2),), ((r'\[[ 가-힣]*\]\[[ 가-힣]*\]- Copyrights', 1),)),
           '파이낸셜뉴스' : (((r'\]', 2),), (('※ 저작권자 ⓒ. 무단 전재-재배포 금지', 1),)),
           '헤럴드경제' : (((r'\]', 2),), (('▶', 1),)),
           '동아일보' : (((r'\]', 2),), 
                      ((r'[ 가-힣=]+[a-zA-Z0-9\.]+@donga\.com', 1), (r'\[동아일보\]', 0), ('ⓒ 동아일보 ', 1),)),
           '문화일보' : (((r'\]', 2),), 
                      (('[ 가-힣=·]+[a-zA-Z0-9\.]+@', 1), (r'\[Copyrightⓒmunhwa\.com', 1),)),
           '연합뉴스' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\(종합\)', 0), (r'\]', 2)), 
                      (('※ 자료 :', 1),(r'\([가-힣]+=연합뉴스\)[ 가-힣]+기자 =', 0), (r'\([가-힣]+=연합뉴스\)', 0), 
                       (r'[a-zA-Z0-9\.]+@yna\.co\.kr', 0))),
           '조세일보' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\[포토\]', 0), (r'\]', 2)), 
                      (('▶▶', 1), ('저작권자 ⓒ 조세일보', 1),)),
           '한겨레' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\]', 2)), 
                     ((r'[ 가-힣]+[a-zA-Z0-9\.]+@hani\.co\.kr▶', 1), ('▶ 한겨레 절친이 되어 주세요', 1), (r'\[한겨레\]', 0),)),
           'MBC 뉴스' : (((r'\]', 2),), 
                        (('◀ 앵커 ▶', 0), ('◀ 캐스터 ▶', 0), ('◀ 리포트 ▶', 0), (r'\[뉴스데스크\]', 0),(r'\[뉴스투데이\]', 0),
                         (r'\[뉴스콘서트\]', 0), (r'\[정오뉴스\]', 0), (r'\[이브닝뉴스\]', 0), ('날씨였습니다', 0), 
                         ('지금까지 스마트리빙이었습니다', 0), ('지금까지 스마트 리빙이었습니다', 0), 
                         ('지금까지 스마트리빙플러스였습니다', 0), ('[ 가-힣]*MBC뉴스 [가-힣]+입니다', 1), (r'[ 가-힣/]+\[저작권자\(c\)', 1),
                         (r'[ 가-힣]+[\(a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]+\[저작권자\(c\)', 1), (r'\[저작권자\(c\) MBC', 1))),
           '디지털타임스' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\]', 2)), 
                         ((r'\[디지털타임스[ 가-힣]+\]', 1),(r'[ =가-힣]*기자 [a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]*[/]+[가-힣]+', 1), 
                          (r'[a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]*[/]+[가-힣]+', 1), ('/인터넷 마케팅팀', 1), ('//[가-힣]+', 1))),
           '서울경제' : ((('오늘의 증시 메모', 4), (r'\[서울경제\]', 0), (r'\[서울경제TV\]', 0), (r'\[투데이포커스\]', 0), (r'\[표\]', 0), 
                       (r'\[S머니\]', 0), (r'\[이슈&워치\]', 0), (r'\[금주의 분양캘린더\]', 0), (r'\]', 2)), 
                      ((r'\[서울[ 가-힣TVtv]+\]', 0), (r'\[[ 가-힣]+경제\]', 0), (r'\[앵커\]', 0), (r'\[기자\]', 0), 
                       (r'\[인터뷰\]', 0), (r'\[이 기사는 증시분석 전문기자 서경뉴스봇', 1), (r'/[ 가-힣=·]+[a-zA-Z0-9\._@]*저작권자', 1),
                       (r'\[사진=', 1), ('저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지',1))),
           '연합뉴스TV' : (((r'\]', 2),), 
                        ((r'\[기자\]', 0), (r'\[앵커\]', 0), (r'\[비즈&\]', 0), (r'\[특별기획\]', 0), (r'\[기업기상도\]', 0), 
                         (r'\[뉴스초점\]', 0), (r'\[CEO풍향계\]', 0), ('[ 가-힣]*연합뉴스TV [가-힣]+입니다.', 1), ('연합뉴스TV : 02', 1))),
           '주간경향' : (((r'\]', 2),), ((r'© 주간경향 \(', 1),)),
           '한경비즈니스' : (((r'\]', 2),), (('▶', 1),)),
           'MBN' : (((r'\]', 2),),
                    (('【 앵커멘트 】', 0), ('【 기자 】', 0), (r'▶[ 가-힣\(☎\)]+:[ /가-힣\'-]*-', 0),
                     (r'\[[ 가-힣]+/[ a-zA-Z0-9@\._]+\]', 1), (r'[a-zA-Z0-9\._]+@[a-zA-Z0-9\._]', 1), 
                     (r'MBN[ ]?뉴스[ 가-힣]+입니다\.', 1), (r'\[MBN 온라인 뉴스팀\]', 1), 
                     (r'\[MBN 온라인뉴스팀\]', 1), ('< Copyright', 1))),
           '매경이코노미' : (((r'\]', 2),), (('▶', 1),)),
           '서울신문' : (((r'\]', 2),), (('▶', 1),)),
           '이데일리' : (((r'\]', 2),), (('▶', 1),)),
           '주간동아' : (((r'\]', 2),), (('▶', 1),)),
           '한국경제' : (((r'\]', 2),), (('▶', 1),)),
           'SBS CNBC' : (((r'\]', 2),), (('▶', 1),))
           }

# patern-삭제할 패턴과 삭제 모드 (모드-0:해당패턴만 삭제/1:해당패턴 뒤 삭제/2:해당패턴 앞 삭제) contents-삭제 대상 
def remove(pattern, contents):
    
    for pa in pattern:
        words = re.findall(pa[0], contents)
#         print(pa)
        
        if len(words) == 0:
            continue
        
        for wor in words:
#             print(wor)
            if pa[1] == 0:
                contents = contents.replace(wor, '')
            elif pa[1] == 1:
                contents = contents.split(wor)[0]
            elif pa[1] == 2:
                contents = contents.split(wor)[1]
            elif pa[1] == 3:
                contents = '-'
            elif pa[1] == 4:
                contents = wor #words 가 하나만 있는게 확실할 때 사용 
                
    return contents

def refin(press, title, contents):
    pattern = patterns[press]
    title = remove(pattern[0], title)
    contents = remove(pattern[1], contents)
    if title == '-':
        contents = title = ''
    
    return [title.strip(), contents.strip()]

if __name__ == "__main__":

    contents = "모바일, 사물인터넷, 빅데이터 등 최신 기술을 보여주는 국내 최대 정보통신기술 전시회인 ‘월드IT쇼 2018’이 개막한 23일 서울 삼성동 코엑스를 찾은 관람객 위로 구름 모양을 한 드론이 떠 있다.▶, 경향비즈 SNS▶[©경향신문(), 무단전재 및 재배포 금지]"
    title = "[포토뉴스]드론이 ‘두둥실’"
#     print(remove(patterns, contents))
    news = refin('경향신문', title, contents)
    print(news[1])
    print(news[0])
