import json
from newsRefining.functions import refin

news = ''

with open('../news_20180106.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)

    for i in range(1, cnt + 1):
        press = jdata['news' + str(i)]['press']
        
        if press == '이코노미스트':
            title = jdata['news' + str(i)]['title']
            contents = jdata['news' + str(i)]['contents']
            
            print(title)
            print(contents)
            
#             news = refin_funcs[press](contents, title)
            news = refin(press, title, contents)
            jdata['news' + str(i)]['contents'] = news[0]
            jdata['news' + str(i)]['title'] = news[1]
            print(jdata['news' + str(i)]['title'])
            print(jdata['news' + str(i)]['contents'])
            print("="*400)

#     f.write()        