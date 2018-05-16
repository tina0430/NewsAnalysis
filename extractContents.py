import json
import re

# 읽어올 json 파일 경로 및 이름 설정
news = ''

with open('./news_20171231.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)
    '''
    func = {'경향신문' : lambda x: x.split('▶')[0],
            '매일경제' : lambda x: x.split('[')[0],
            '세계일보' : lambda x: x.split('')[0]}
    for i in range(1, cnt+1):
        press = jdata['news'+str(i)]['press']
        contents = jdata['news'+str(i)]['contents']
        jdata['news'+str(i)]['contents'] = func[press](contents)
        print(contents)
    ''' 
    for i in range(1, cnt+1):
        if jdata['news'+str(i)]['press'] == '세계일보':
#             print(jdata['news'+str(i)]['press'])
            contents = jdata['news'+str(i)]['contents']
            #세종=안용성 기자, 염유섭 기자 ysahn@segye.comⓒ 세상을 보는 눈, 글로벌 미디어
            fi = re.findall('[가-힣]{2,} [가-힣]*기자', contents)
            print(fi)
            if len(fi) != 0:
                contents = contents.split(fi[0])[0]
            else:
                contents = contents.split('ⓒ 세상을 보는 눈, 글로벌 미디어')[0]
            print(contents)
            
        #경향신문
        #▶, 경향비즈 SNS▶[©경향신문(), 무단전재 및 재배포 금지]
        
        #매일경제
        #[디지털뉴스국 김수연 인턴기자][ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[디지털뉴스국][ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[디지털뉴스국][ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[매경 부동산센터 이다연 기자][ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[강영운 기자] [매일경제 공식 페이스북] [오늘의 인기뉴스] [매경 프리미엄] [ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[기획취재팀 = 한예경 기자(차장) / 박준형 기자 / 정지성 기자 / 고민서 기자 / 김종훈 기자 / 이윤식 기자 / 노승환 기자 / 이희수 기자] [매일경제 공식 페이스북] [오늘의 인기뉴스] [매경 프리미엄] [ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]
        #[도쿄 = 황형규 특파원] [매일경제 공식 페이스북] [오늘의 인기뉴스] [매경 프리미엄][ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]