import json
from newsRefining.functions import refin_news
import time

def refin_new_day(file_name):
    news = ''
    start_time = time.time()
#     file_name = '../news_'+date+'.json'
    with open(file_name, 'r', encoding='utf-8') as f:
        jdata = json.load(f)
        cnt = len(jdata)
     
        for i in range(1, cnt + 1):
            press = jdata['news' + str(i)]['press']
            title = jdata['news' + str(i)]['title']
            contents = jdata['news' + str(i)]['contents']
        
            news = refin_news(press, title, contents)
            jdata['news' + str(i)]['title'] = news[0]
            jdata['news' + str(i)]['contents'] = news[1]
    #         print(jdata['news' + str(i)]['title'])
    #         print(jdata['news' + str(i)]['contents'])
    print(jdata)
    return jdata
#     data 가 인풋일 경우
#     file_name = '../news_'+date+'_refin.json'
#     with open(file_name, 'w', encoding='utf-8') as f:
#         json.dump(jdata, f, ensure_ascii=False, indent="\t")
    
    print(start_time - time.time())    
    
if __name__ == "__main__":
    refin_new_day('20180404')
    