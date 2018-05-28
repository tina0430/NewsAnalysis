import json
from newsRefining.functions import refin

news = ''

with open('../news_20180101.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)

    for i in range(1, cnt + 1):
        press = jdata['news' + str(i)]['press']
        
 
        title = jdata['news' + str(i)]['title']
        contents = jdata['news' + str(i)]['contents']

        if press =='SBS CNBC':    
            print(title)
            print(contents)
            news = refin(press, title, contents)
            jdata['news' + str(i)]['title'] = news[0]
            jdata['news' + str(i)]['contents'] = news[1]
            print(jdata['news' + str(i)]['title'])
            print(jdata['news' + str(i)]['contents'])
            print("="*400)


#     f.write()        