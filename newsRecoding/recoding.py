
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

#         write_json(words, result_directory)
        return words


# def get_news_file_list(folder_route):
#     if os.path.isdir(folder_route) == False:
#         return None
#      
#     news_pattern = re.compile('.*news_[\d]+.json$')
#     file_list = []
#     for file in os.listdir(folder_route):
#         file_route = folder_route + '\\' + file
#          
#         if os.path.isfile(file_route):
#             if news_pattern.match(file_route) != None:
#                 file_list.append(file_route)
#                  
#         elif os.path.isdir(file_route):
#             file_list.extend(get_news_file_list(file_route + '\\'))
#      
#     return file_list


if __name__ == '__main__':
    news_directory = r'./'      
    result_directory = r'./'
    
    json_data = {"뉴스":{"삼성":"어플리케이션","운동":"어플리케이션","노래":" 은산"}}
    json_data = json.dumps(json_data)
    
    start_time = time.time()
    
    print("Recoding 시작")
    with open('recode.json','r',encoding="utf-8") as b:
        dic = json.load(b)
        
    replace_all(dic, json_data)
#     news_list = get_news_file_list(news_directory)
#     if news_list is not None:
#         for news_name in news_list:
#             replace_all(news_name, dic, result_directory)

    end_time = time.time()
    print('Recoding 끝 - %s 초' % str(end_time - start_time) )


    