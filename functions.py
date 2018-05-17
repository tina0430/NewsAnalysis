import re 

def segeu_ilbo(contents):
    sp = re.findall('[.][가-힣]{0,2}[=]?[가-힣]{2,} [가-힣]*기자', contents)
    print(sp)
    contents = contents.split(sp[0]) if len(sp) != 0 else contents.split('ⓒ 세상을 보는 눈, 글로벌 미디어')
    return contents[0] + '.'

extract_contesnt = {'경향신문' : lambda x: x.split('▶')[0],
        '매일경제' : lambda x: x.split('[')[0],
        '세계일보' : segeu_ilbo,
        '이코노미스트' : lambda x: x,
        '중앙SUNDAY' : lambda x: x,
        '한국경제TV' : lambda x: x,
        'SBS 뉴스' : lambda x: x,
        '국민일보' : lambda x: x,
        '머니S' : lambda x: x,
        '신동아' : lambda x: x,
        '조선비즈' : lambda x: x,
        '중앙일보' : lambda x: x,
        '한국일보' : lambda x: x,
        'YTN' : lambda x: x,
        '뉴시스' : lambda x: x,
        '머니투데이' : lambda x: x,
        '아시아경제' : lambda x: x,
        '조선일보' : lambda x: x,
        '파이낸셜뉴스' : lambda x: x,
        '헤럴드경제' : lambda x: x,
        '동아일보' : lambda x: x,
        '문화일보' : lambda x: x,
        '연합뉴스' : lambda x: x,
        '조세일보' : lambda x: x,
        '한겨레' : lambda x: x,
        'MBC 뉴스' : lambda x: x,
        '디지털타임스' : lambda x: x,
        '서울경제' : lambda x: x,
        '연합뉴스TV' : lambda x: x,
        '주간경향' : lambda x: x,
        '한경비즈니스' : lambda x: x,
        'MBN' : lambda x: x,
        '매경이코노미' : lambda x: x,
        '서울신문' : lambda x: x,
        '이데일리' : lambda x: x,
        '주간동아' : lambda x: x,
        '한국경제' : lambda x: x,
        'SBS CNBC' : lambda x: x
        }