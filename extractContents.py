import json
from functions import extract_contesnt
news = ''

with open('./news_20180110.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)

    for i in range(1, cnt + 1):
        news = []
        press = jdata['news' + str(i)]['press']
        if press == '아시아경제':
#             print(i, " : ", press)
            title = jdata['news' + str(i)]['title']
            contents = jdata['news' + str(i)]['contents']
            print(title)
            print(contents)
            news = extract_contesnt[press](contents, title)
            jdata['news' + str(i)]['contents'] = news[0]
            jdata['news' + str(i)]['title'] = news[1]
            print(jdata['news' + str(i)]['title'])
            print(jdata['news' + str(i)]['contents'])
            print("="*300)

            