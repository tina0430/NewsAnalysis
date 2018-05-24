import json
from newsRefining.functions import refin_funcs 
news = ''

with open('./news_20180302.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)

    for i in range(1, cnt + 1):
        news = []
        press = jdata['news' + str(i)]['press']
        if press == '디지털타임스':
#             print(i, " : ", press)
            title = jdata['news' + str(i)]['title']
            contents = jdata['news' + str(i)]['contents']
            print(title)
            print(contents)
            news = refin_funcs[press](contents, title)
            jdata['news' + str(i)]['contents'] = news[0]
            jdata['news' + str(i)]['title'] = news[1]
            print(jdata['news' + str(i)]['title'])
            print(jdata['news' + str(i)]['contents'])
            print("="*300)

            