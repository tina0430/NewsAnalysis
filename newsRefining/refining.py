import json
from newsRefining.functions import refin, moneyToday, ytn, hankook

news = ''

with open('../news_20180106.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)

    for i in range(1, cnt + 1):
        press = jdata['news' + str(i)]['press']
        
 
        title = jdata['news' + str(i)]['title']
        contents = jdata['news' + str(i)]['contents']
        
        if press == '머니투데이':             
            news = moneyToday(press, title, contents)
#         if press == 'YTN':             
#             news = ytn(press, title, contents)
#         if press == '한국일보':             
#             news = ytn(press, title, contents)
        elif press == '중앙일보':     
            print(title)
            print(contents)
            news = refin(press, title, contents)
            jdata['news' + str(i)]['title'] = news[0]
            jdata['news' + str(i)]['contents'] = news[1]
            print(jdata['news' + str(i)]['title'])
            print(jdata['news' + str(i)]['contents'])
            print("="*400)


#     f.write()        