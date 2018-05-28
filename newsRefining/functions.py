import re 

def ytn(press, title, contents):
    if press != 'YTN':
        print('wrong data')
        return [title, contents]
    
    if title.rfind('[자막뉴스]') != -1:
        writer = re.findall(r'[ 가-힣\ㅣ]+\[저작권자(c)', contents)
        if len(writer) != 0:
            contents = contents.split(writer[0])[0]
    
    if contents.rfind('[앵커]') != -1:
        for i in ('[앵커]', '[기자]'):
            contents = contents.replace(i, '')
        writer = re.findall(r'[지금까지 ]{,5}YTN [가-힣]+[\[a-zA-Z0-9@ytn.co.kr\]]*입니다', contents)
        if len(writer) != 0:
            contents = contents.split(writer[0])[0]
            
    reporter = re.findall(r'[YTN ]{,4}[ 가-힣]+\[[a-zA-Z0-9\.]+@ytn.co.kr\]\[저작권자', contents)
    if len(reporter) != 0:
        contents = contents.split(reporter[0])[0]
        
    contents = contents.split('[저작권자(c) YTN & YTN PLUS 무단전재 및 재배포 금지]')[0]
    contents = contents.split('[사진제공 = CJ CGV]')[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [title.strip(), contents.strip()]

def moneyToday(press, title, contents):
    if press != '머니투데이':
        print('wrong data')
        return [title, contents]
    
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

def edaily(press, title, contents):
    if press != '이데일리':
        print('wrong data')
        return [title, contents]

    writer = re.findall(r'\[[ 가-힣=]*이데일리[ 가-힣 \(\)=,?&?]+\]', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '').strip()
        writer[0] = writer[0].split('이데일리')[1].strip()
        for i in ('기자', '특파원', ']'):
            writer[0] = writer[0].split(i)[0].strip()
        contents = contents.split(writer[0]+ ' (')[0]
    
    marketpoint = re.findall(r'\[이데일리 MARKETPOINT\]', contents)
    if len(marketpoint) != 0:
        contents = contents.replace('[이데일리 MARKETPOINT]','')[0]
        contents = contents.split('마켓포인트 (world@edaily.co.kr)')[0]
        
    contents = contents.split('edaily.co.kr)')[0]
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    
    return [title.strip(), contents.strip()]

def hankook(press, title, contents):
    if press != '한국경제':
        print('wrong data')
        return [title, contents]

    writer = re.findall(r'\[[ 가-힣 \(\)=,?&?/]+\]', contents)
    if len(writer) != 0:
        contents = contents.replace(writer[0], '')
        for i in ('[', '기자', ']'):
            writer[0] = writer[0].replace(i, '').strip()
        contents = contents.split(writer[0])[0]
    
    location = re.findall('[가-힣]+=$', contents)
    if len(location) != 0:
        contents = contents.replace(location[0], '')
        
    contents = contents.split('[] [] []ⓒ 한국경제 &, 무단전재 및 재배포 금지')[0]
    contents = contents.split('ⓒ 한국경제 &, 무단전재 및 재배포 금지')[0]
    
    title = title.split(']')
    title = title[0] if len(title) == 1 else title[1]
    return [title.strip(), contents.strip()]


patterns= {'경향신문' : (((r'\]\[', 2), (r'\]', 2)), (('▶', 1),)),
           '매일경제' : (((r'\]\[', 2), (r'\]', 2)), ((r'\[', 1),)),
           '세계일보' : (((r'\]\[', 2), (r'\]', 2)), 
                      ((r'[a-zA-Z0-9\._]+@segye.com', 0),('[ =,가-힣]*ⓒ', 1), ('ⓒ 세상을 보는 눈, 글로벌 미디어', 1))),
           '이코노미스트' : (((r'\]\[', 2), (r'\]', 2)), 
                         ((r'([ 가-힣]*[-_\.0-9a-zA-Z]+@joongang\.co\.kr\[ⓒ 이코노미스트)', 1), 
                          ('※', 1), (r'[ 가-힣a-zA-Z]*\[ⓒ 이코노미스트', 1))),
           '한국경제TV' : (((r'\[국고처', 3), (r'\[인사\]',3 )), 
                        ((r'\(위의 AI인공지능 점수는 재무 데이터를 기반으로', 1), ('자세한 내용은 한국경제TV 다시보기', 1), ('ⓒ 한국경제TV', 1), 
                         (r'\([-_\.0-9a-zA-Z]*@wowtv\.co\.kr\)', 1), ('[가-힣]+[ ]*기자[ ]*$', 0), ('[가-힣]+[ ]*PD[ ]*$', 0),
                         ('디지털 뉴스부', 0), ('디지털뉴스부', 0), ('라이온봇기자', 0))),
           'SBS 뉴스' : (((r'\]\[', 2), (r'\]', 2)), #흠 
                        (('※ ⓒ SBS', 1), (r'\(영상취재 :', 1), (r'\(영상편집 :', 1), (r'\(사진=', 1), ('<기자>', 0), ('<앵커>', 0), 
                         (r'[가-힣 ]{2,}기자\(', 1))),
           '국민일보' : (((r'\]\[', 2), (r'\]', 2)), #흠 
                      (('뉴시스GoodNews paper ⓒ', 1), ('GoodNews paper ⓒ', 1), ('각 부 종합,', 1), ('[가-힣]+=[가-힣]+', 1), 
                       ('[가-힣 ]+기자', 1))),
           '머니S' : (((r'\]\[', 2), (r'\]', 2)), ((r'\.[가-힣  ]{2,5}기자$', 1),)),
           '신동아' : (((r'\]\[', 2), (r'\]', 2)), 
                     ((r'[\| ]*[0-9가-힣  ]+기자[ ]*[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', 1),(r'[-_\.0-9a-zA-Z]+@[-_\.0-9a-zA-Z]+', 1),
                      (r'\[신동아\]', 0), ('[\| ]*[0-9가-힣  ]+\|', 1))),
           '조선비즈' : (((r'\]\[', 2), (r'\]\[', 2), (r'\]', 2)), ((r'\[[가-힣0-9A-Za-z@\. =]*\]chosunbiz.com', 1),)),
           '중앙일보' : (((r'\[인사\]', 2), (r'\]', 2)), 
                      ((r'[ =가-힣]+[0-9A-Za-z\.]+@joongang.co.kr▶', 1), (r'[ =가-힣]+[기자]▶', 1),
                       (r'\[ⓒ 조인스랜드 : JTBC', 1), ('▶모바일에서 만나는 중앙일보', 1))),
           '한국일보' : (((r'\]\[', 2), (r'\]', 2)), 
                      ((r'[ 가-힣 =]+[ 0-9A-Za-z\.]+@hankookilbo\.com\[ⓒ 한국일보', 1), (r'[가-힣 ]+=?[ 가-힣]+기자[ ]?\[ⓒ 한국일보', 1), 
                       (r'[ 가-힣 =]+[ 0-9A-Za-z\.]+@beautyhankook\.com\[ⓒ 한국일보', 1), (r'\[ⓒ 한국일보\(', 1),)),
           '뉴시스' : (((r'\]\[', 2), (r'\]', 2)), 
                     ((r'\【[ 가-힣]+=뉴시스\】[ 가-힣]+기자[ =]+', 0), (r'[a-zA-Z0-9]+@newsis.com', 0), (r'\(사진[ =가-힣]+제공\)', 1),
                      ('공감언론 뉴시스가 독자 여러분의 소중한 제보를 기다립니다', 1))),
           '아시아경제' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\[포토\]', 0), (r'\]\[', 2), (r'\]', 2)), 
                        ((r'\[[ 가-힣=\]*아시아경제[ 가-힣=]+\]', 0), (r'\[', 1), ('아시아경제 ', 1), (']', 1), 
                         (r'[ 가-힣 =]+[a-zA-Z0-9\._]+@asiae.co.kr', 1))),
           '조선일보' : (((r'\]\[', 2), (r'\]', 2)), ((r'\[[ 가-힣]*\]\[[ 가-힣]*\]- Copyrights', 1),)),
           '파이낸셜뉴스' : (((r'\]\[', 2), (r'\]', 2)), (('※ 저작권자', 1),)),
           '헤럴드경제' : (((r'\[인사\]', 3), (r'\[부고\]', 3), (r'\]\[', 2), (r'\]', 2)),
                        (('(본 기사는 헤럴드경제로부터 제공받은 기사입니다.)', 0), (r'\[헤럴드경제=[ 가-힣]+\]', 0),(r'［헤럴드경제=[ 가-힣]+］', 0),
                         (r'[가-힣]+ 기자/[ a-zA-Z0-9\.]+@[ a-zA-Z0-9\.]*- Copyrights', 1), 
                         (r'[a-zA-Z0-9\.]+@[ a-zA-Z0-9\.]*- Copyrights', 1), ('- Copyrights ⓒ 헤럴드경제', 1))),
           '동아일보' : (((r'\]\[', 2), (r'\]', 2)), 
                      ((r'[ 가-힣=]+[a-zA-Z0-9\.]+@donga\.com', 1), (r'\[동아일보\]', 0), ('ⓒ 동아일보 ', 1),)),
           '문화일보' : (((r'\]\[', 2), (r'\]', 2)), 
                      (('[ 가-힣=·]+[a-zA-Z0-9\.]+@', 1), (r'\[Copyrightⓒmunhwa\.com', 1),)),
           '연합뉴스' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\(종합\)', 0), (r'\]\[', 2), (r'\]', 2)), 
                      (('※ 자료 :', 1),(r'\([가-힣]+=연합뉴스\)[ 가-힣]+기자 =', 0), (r'\([가-힣]+=연합뉴스\)', 0), 
                       (r'[a-zA-Z0-9\.]+@yna\.co\.kr', 0))),
           '조세일보' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\[포토\]', 0), (r'\[탐방\]', 0), (r'\]\[', 2), (r'\]', 2)), 
                      (('▶▶', 1), ('저작권자 ⓒ 조세일보', 1),)),
           '한겨레' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\]', 2)), 
                     ((r'[ 가-힣]+[a-zA-Z0-9\.]+@hani\.co\.kr▶', 1), ('▶ 한겨레 절친이 되어 주세요', 1), (r'\[한겨레\]', 0),)),
           'MBC 뉴스' : (((r'\]\[', 2), (r'\]', 2)), 
                        (('◀ 앵커 ▶', 0), ('◀ 캐스터 ▶', 0), ('◀ 리포트 ▶', 0), (r'\[뉴스데스크\]', 0),(r'\[뉴스투데이\]', 0),
                         (r'\[뉴스콘서트\]', 0), (r'\[정오뉴스\]', 0), (r'\[이브닝뉴스\]', 0), ('날씨였습니다', 0), 
                         ('지금까지 스마트리빙이었습니다', 0), ('지금까지 스마트 리빙이었습니다', 0), 
                         ('지금까지 스마트리빙플러스였습니다', 0), ('[ 가-힣]*MBC뉴스 [가-힣]+입니다', 1), (r'[ 가-힣/]+\[저작권자\(c\)', 1),
                         (r'[ 가-힣]+[\(a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]+\[저작권자\(c\)', 1), (r'\[저작권자\(c\) MBC', 1))),
           '디지털타임스' : (((r'\[부고\]', 3), (r'\[인사\]', 3), (r'\]\[', 2), (r'\]', 2)), 
                         ((r'\[디지털타임스[ 가-힣]+\]', 1),(r'[ =가-힣]*기자 [a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]*[/]+[가-힣]+', 1), 
                          (r'[a-zA-Z0-9\.]+@[a-zA-Z0-9\.\)]*[/]+[가-힣]+', 1), ('/인터넷 마케팅팀', 1), ('//[가-힣]+', 1))),
           '서울경제' : ((('오늘의 증시 메모', 4), (r'\[서울경제\]', 0), (r'\[서울경제TV\]', 0), (r'\[투데이포커스\]', 0), (r'\[표\]', 0), 
                       (r'\[S머니\]', 0), (r'\[이슈&워치\]', 0), (r'\[금주의 분양캘린더\]', 0), (r'\]\[', 2), (r'\]', 2)), 
                      ((r'\[서울[ 가-힣TVtv]+\]', 0), (r'\[[ 가-힣]+경제\]', 0), (r'\[앵커\]', 0), (r'\[기자\]', 0), 
                       (r'\[인터뷰\]', 0), (r'\[이 기사는 증시분석 전문기자 서경뉴스봇', 1), (r'/[ 가-힣=·]+[a-zA-Z0-9\._@]*저작권자', 1),
                       (r'\[사진=', 1), ('저작권자 ⓒ 서울경제, 무단 전재 및 재배포 금지',1))),
           '연합뉴스TV' : (((r'\]\[', 2), (r'\]', 2)), 
                        ((r'\[기자\]', 0), (r'\[앵커\]', 0), (r'\[비즈&\]', 0), (r'\[특별기획\]', 0), (r'\[기업기상도\]', 0), 
                         (r'\[뉴스초점\]', 0), (r'\[CEO풍향계\]', 0), ('[ 가-힣]*연합뉴스TV [가-힣]+입니다.', 1), ('연합뉴스TV : 02', 1))),
           '주간경향' : (((r'\]\[', 2), (r'\]', 2)), ((r'© 주간경향 \(', 1),)),
           '한경비즈니스' : (((r'\]\[', 2), (r'\]', 2)), (('▶', 1),)),
           'MBN' : (((r'\]\[', 2), (r'\]', 2)),
                    (('【 앵커멘트 】', 0), ('【 기자 】', 0), (r'▶[ 가-힣\(☎\)]+:[ /가-힣\'-]*-', 0),
                     (r'\[[ 가-힣]+/[ a-zA-Z0-9@\._]+\]', 1), (r'[a-zA-Z0-9\._]+@[a-zA-Z0-9\._]', 1), 
                     (r'MBN[ ]?뉴스[ 가-힣]+입니다\.', 1), (r'\[MBN 온라인 뉴스팀\]', 1), 
                     (r'\[MBN 온라인뉴스팀\]', 1), ('< Copyright', 1))),
           '매경이코노미' : (((r'\]\[', 2), (r'\]', 2)), (('\[', 1),)),
           '서울신문' : (((r'\]\[', 2), (r'\]', 2)), 
                      ((r'[ 가-힣]+[a-zA-Z0-9\._]+@seoul\.co\.kr▶', 1), ('▶  재미있는 세상', 1), 
                        ('나우뉴스부★', 1), (r'▶ \[\]▶ \[\]'), (r'\[서울신문\]', 0))),
           '주간동아' : (((r'\]\[', 2), (r'\]', 2)), 
                      ((r'\[주간동아\]', 0), (r'\|[ 가-힣·=]+[a-zA-Z0-9@\._]+', 1), 
                       (r'[ 가-힣]+기자[ ]?[a-zA-Z0-9\._]+@donga.com', 1))),
           'SBS CNBC' : (((r'\[인사\]', 3), (r'\[부고\]', 3)), (r'\]\[', 2), 
                         (('SBSCNBC[ 가-힣]+입니다', 1),(r'\(자세한 내용은 동영상을 시청하시기 바랍니다', 1), ('[ 가-힣]+기자였습니다', 1), 
                          (r'[a-zA-Z]+[ 가-힣]+기자[ ]?\([a-zA-Z0-9\._]+@sbs\.co\.kr', 1), ('지금까지[ 가-힣]+습니다', 1), ('지금까지  SBSCNBC', 1),
                          (r'\[SBSCNBC 뉴미디어팀\]', 1), ('[ 가-힣]+기자 잘 들었습니다', 1)))
           }


def remove(pattern, contents):
    
    for pa in pattern:
        words = re.findall(pa[0], contents)
        
        if len(words) == 0:
            continue
        
        for wor in words:
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

def refin_news(press, title, contents):
    exception = {'머니투데이':moneyToday, 'YTN':ytn, '이데일리':edaily, '한국경제':hankook}
    if press in exception.keys():
        return exception[press](press, title, contents)

    if press == '중앙SUNDAY':
        return ['','']

    pattern = patterns[press]
    title = remove(pattern[0], title)
    contents = remove(pattern[1], contents)
    
    if title == '-':
        contents = title = ''
    
    return [title.strip(), contents.strip()]

if __name__ == "__main__":
    contents = "모바일, 사물인터넷, 빅데이터 등 최신 기술을 보여주는 국내 최대 정보통신기술 전시회인 ‘월드IT쇼 2018’이 개막한 23일 서울 삼성동 코엑스를 찾은 관람객 위로 구름 모양을 한 드론이 떠 있다.▶, 경향비즈 SNS▶[©경향신문(), 무단전재 및 재배포 금지]"
    title = "[포토뉴스]드론이 ‘두둥실’"
    news = refin_news('경향신문', title, contents)
    print(news[1])
    print(news[0])
