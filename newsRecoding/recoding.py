import json
import re
import pandas as pd 
from collections import OrderedDict
import time


def replace_all(dic):
    words = OrderedDict()
    def write_json(words):
        file = open('re_'+ file_name,'w',encoding='utf-8')
        json.dump(words, file, ensure_ascii = False,indent = 1)
            

        
#     i = 1
    j = 1
    for a, b in jdata.items():
        for roof in range(3):
            text = jdata[a][roof]
            
            text = re.sub(r"['(']\w+[')']", "", text)
            text = re.sub(r"['(']\w+\W\w+[')']", "", text)
            text = re.sub(r"\d+[일]","",text)
            text = re.sub(r"['(']\d*\W\d+\W[')']", "", text)
            text = re.sub(r"['(']\W\d*\W\d+\W[')']", "", text)
                  
            for old, new in dic.items():
                if roof == 1:
                    break
                
                text = text.replace(old, new)
            
            if roof == 0:
                text1 = text
            elif roof == 1:
                text2 = text
            elif roof == 2:
                text3 = text
                     

            if roof == 2:
                words["news%d"%j] = {"press":text2,"contents":text1,"title":text3}
                write_json(words)
                j += 1
#         i += 1
#                 
#         if i == 50:
#             break
#                
if __name__ == '__main__':
    with open('recode.json','r',encoding="utf-8") as b:
        dic = json.load(b)
    
    file_name = "news_20170403.json"
    jdata = pd.read_json('./'+ file_name, encoding='utf-8')
    start_time = time.time()
    print("Recoding 시작")
    replace_all(dic)
    end_time = time.time()
    print('Recoding 끝 - %s 초' % str(end_time - start_time) )



    