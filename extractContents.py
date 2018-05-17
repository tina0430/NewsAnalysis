import json
from functions import extract_contesnt
news = ''

with open('./news_20180325.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)
    cnt = len(jdata)

    for i in range(1, cnt + 1):
        press = jdata['news' + str(i)]['press']
        if press == '국민일보':
#             print(i, " : ", press)
            title = jdata['news' + str(i)]['title']
            contents = jdata['news' + str(i)]['contents']
            print(jdata['news' + str(i)]['title'])
            print(jdata['news' + str(i)]['contents'])
            jdata['news' + str(i)]['contents'] = extract_contesnt[press](contents, title)
            print(jdata['news' + str(i)]['contents'])
            print("="*300)

            