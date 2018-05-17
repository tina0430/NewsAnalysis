import re 

def gyeong_hyang(contents, title):
    contents = contents.split('▶')[0]
    return contents

def maeil(contents, title):
    contents = contents.split('[')[0]
    return contents

def segeu_ilbo(contents, title):
    sp = re.findall('[.][가-힣]{0,2}[=]?[가-힣]{2,} [가-힣]*기자', contents)
    if len(sp) != 0:
        contents = contents.split(sp[0])[0] + '.'  
    else: 
        contents = contents.split('ⓒ 세상을 보는 눈, 글로벌 미디어')[0]
    return contents

def economist(contents, title):
    contents = contents.split('[ⓒ 이코노미스트(')[0]
    contents = contents.split('※ 필자는')[0]
    
    email = re.findall(r'([-_\.0-9a-zA-Z]*@joongang\.co\.kr)', contents)
    if len(email) != 0:
        contents = contents.split(email[0])[0]
    
    end = re.findall('※?[가-힣a-zA-Z0-9 ()=]+$', contents)
    if len(end) != 0:
        contents = contents.replace(end[0], '')
    return contents

#만족
def han_gyeong(contents, title):
    for i in ('[국고처', '[인사]'):
        if title.rfind(i) != -1:
            return ''
    contents = contents.split('(위의 AI인공지능 점수는 재무 데이터를 기반으로 전체 상장 종목과 비교')[0]
    contents = contents.split('자세한 내용은 한국경제TV 다시보기를 통해 볼 수 있습니다.')[0]
    contents = contents.split('ⓒ 한국경제TV')[0]
    
    email = re.findall(r'([-_\.0-9a-zA-Z]*@wowtv\.co\.kr)', contents)
    if len(email) != 0:
        print(email)
        contents = contents.split(email[0])[0]
    
    end = re.findall('[가-힣]+[ ]*기자+[ ]*$', contents)
    if len(end) != 0:
        contents = contents.replace(end[0], '')
    
    end = re.findall('[가-힣]+[ ]*PD+[ ]*$', contents)
    if len(end) != 0:
        contents = contents.replace(end[0], '')
        
    for i in ['디지털 뉴스부', '디지털뉴스부', '라이온봇기자']:
        contents = contents.replace(i, '')
    return contents
    


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
        print(email)
        contents = contents.split(email[0])[0]
    return contents

def gugmin(contents, title):
    pass

'''
※ 필자는 중앙일보 ‘더, 오래팀’ 기획위원이다.

서명수 중앙일보 ‘더, 오래팀’ 기획위원

[정기구독 신청] [콘텐트 구매]
[ⓒ 이코노미스트(jmagazine.joins.com) and JTBC Content Hub Co., Ltd. 무단 전재 및 재배포 금지]
'''

extract_contesnt = {'경향신문' : gyeong_hyang,
                    '매일경제' : maeil,
                    '세계일보' : segeu_ilbo,
                    '이코노미스트' : economist,
                    '중앙SUNDAY' : lambda x, y: x+y,   #제외
                    '한국경제TV' : han_gyeong,
                    'SBS 뉴스' : sbsNews,
                    '국민일보' : lambda x, y: x+y,
                    '머니S' : lambda x, y: x+y,
                    '신동아' : lambda x, y: x+y,
                    '조선비즈' : lambda x, y: x+y,
                    '중앙일보' : lambda x, y: x+y,
                    '한국일보' : lambda x, y: x+y,
                    'YTN' : lambda x, y: x+y,
                    '뉴시스' : lambda x, y: x+y,
                    '머니투데이' : lambda x, y: x+y,
                    '아시아경제' : lambda x, y: x+y,
                    '조선일보' : lambda x, y: x+y,
                    '파이낸셜뉴스' : lambda x, y: x+y,
                    '헤럴드경제' : lambda x, y: x+y,
                    '동아일보' : lambda x, y: x+y,
                    '문화일보' : lambda x, y: x+y,
                    '연합뉴스' : lambda x, y: x+y,
                    '조세일보' : lambda x, y: x+y,
                    '한겨레' : lambda x, y: x+y,
                    'MBC 뉴스' : lambda x, y: x+y,
                    '디지털타임스' : lambda x, y: x+y,
                    '서울경제' : lambda x, y: x+y,
                    '연합뉴스TV' : lambda x, y: x+y,
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