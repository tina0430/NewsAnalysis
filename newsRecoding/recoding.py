
import json
import re
import pandas as pd 
from collections import OrderedDict
import time

import os

def replace_all(re_dict, json_data):
#     def write_json(words, result_directory):
#         if os.path.isdir(result_directory) == False:
#             os.makedirs(result_directory, exist_ok=True)
#              
#         json_name = file_name.split(sep='\\')[-1]
#         new_name = result_directory + '\\re_' + json_name
#  
#         file = open(new_name,'w',encoding='utf-8')
#         json.dump(words, file, ensure_ascii = False,indent = 1)
         
    jdata = pd.read_json(json_data, encoding='utf-8')
    
    words = OrderedDict()

    j = 1
    for a in jdata.keys():
        for roof in range(3):
            text = jdata[a][roof]
            text = re.sub(r"['(']\w+[')']", "", text)
            text = re.sub(r"['(']\w+\W\w+[')']", "", text)
            text = re.sub(r"\d+[일]","",text)
            text = re.sub(r"['(']\d*\W\d+\W[')']", "", text)
            text = re.sub(r"['(']\W\d*\W\d+\W[')']", "", text)
                  
            for old, new in re_dict.items():
                if roof == 1:
                    break
                
                if text.find(old) == 0:
                    text = text.replace(old, new, 1)
                    
                text = text.replace(old, new)
            
            if roof == 0:
                text1 = text
            elif roof == 1:
                text2 = text
            elif roof == 2:
                text3 = text
                     

            if roof == 2:
                words["news%d"%j] = {"press":text2,"contents":text1,"title":text3}
                j += 1

    if len(words) > 0:
        return words

def load_recode_dict(dict_route):
    with open(dict_route,'r',encoding="utf-8") as b:
        dic = json.load(b)
    return dic

if __name__ == '__main__':
    news_directory = r'./'      
    result_directory = r'./'
    
    json_data = {"뉴스":{"삼성":"어플리케이션","운동":"어플리케이션","노래":" 은산"}}
    json_data = json.dumps(json_data)
    
    start_time = time.time()
    
    print("Recoding 시작")
    
    dic = load_recode_dict(r'../files/dictionaries/recode_dictionary.json')
    replace_all(dic, json_data)

    end_time = time.time()
    print('Recoding 끝 - %s 초' % str(end_time - start_time) )


    