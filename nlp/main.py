# This Python file uses the following encoding: utf-8

from nlp import knlp, count, filter


import os
import re
import pandas
import time
from datetime import datetime

import itertools
import multiprocessing

def get_newsname(news_route):
    return news_route.split('\\')[-1].split('.')[0]

class Settings():
    news_route = None
    konlp_class = None
    konlp_function = None
    filter_route = None
    result_route = None
    
    @classmethod
    def settings(cls, settings_route):
        df = pandas.read_csv(settings_route, header = None)
        trans_df = df.transpose()
        settings = trans_df.rename(columns=df[:][0]).drop(0).reset_index(drop=True)
        
        cls.news_route = settings.news_folder[0].replace('\u202a','')
        cls.konlp_class = settings.konlp_engine[0].replace('\u202a','')
        cls.konlp_function = settings.konlp_function[0].replace('\u202a','')
        cls.filter_route = settings.filter_dictionary[0].replace('\u202a','')
        cls.result_route = settings.result_folder[0].replace('\u202a','')

class News():
    def __init__(self, news_route):
        self.route = news_route
        self.name = get_newsname(news_route)
        self.news = None
        self.nouns = None
        self.counts = None
        self.result = None
        self.process_log = None
        
    def write_result(self, route = None):
        if self.result is None:
            print('result in empty.')
            return
        
        if route is None or os.path.isdir(route) == False:
            route = ''
        else:
            route = route + '\\'
        
        filename = route + '{}_{}_{}_{}.csv'.format(self.name, 'nouns', 'count', 'filter')
        self.result.to_csv(filename, sep = '\t', index = False)
    
    def news_process(self):
        Settings.settings('settings.csv')
        start_read_news = time.time()

        self.news = knlp.read_news(self.route)
        end_read_news = time.time()
        
        log_read_news = 'os{} : {} - read_news() - {}'.format(os.getpid(),
                                                            self.name,
                                                            str(end_read_news - start_read_news))
        print(log_read_news)
        
        start_konlpy = time.time()
        self.nouns = knlp.get_KoNLP(self.news, Settings.konlp_class, Settings.konlp_function)
        self.nouns = list(itertools.chain.from_iterable(self.nouns))
        end_konlp = time.time()
        
        log_nouns = 'os{} : {} - Twitter.nouns() - {}'.format(os.getpid(),
                                                              self.name,
                                                              str(end_konlp - start_konlpy))
        print(log_nouns)

        start_count = time.time()
        count_data = count.get_unique_count(self.nouns)
        self.counts = pandas.DataFrame({'word':list(count_data.keys()), 'count':list(count_data.values())})
        self.counts = self.counts.sort_index(axis = 1, ascending  = False)
        end_count = time.time()
        
        log_count = 'os{} : {} - count.get_unique_count() - {}'.format(os.getpid(),
                                                                       self.name,
                                                                       str(end_count - start_count))
        print(log_count)
        
        start_filter = time.time()
        self.result = filter.filter_count(self.counts, Settings.filter_route)
        end_filter = time.time()
        
        log_filter = 'os{} : {} - filter.filter_count() - {}'.format(os.getpid(),
                                                                     self.name,
                                                                     str(end_filter - start_filter))
        print(log_filter)
        self.process_log = '\n'.join([log_read_news, log_nouns, log_count, log_filter])
        self.write_result(Settings.result_route)
            

def get_news_file_list(folder_route):
    if os.path.isdir(folder_route) == False:
        return None
    
    news_pattern = re.compile('^news_[\d]+.json$')
    file_list = []
    for file in os.listdir(folder_route):
        #if file.endswith('json'):
        if news_pattern.match(file) != None:
            file = '\\' + file
            file_list.append(folder_route + file)
    
    return file_list

def run_News(news_object):
    if news_object is None:
        return None
    
    news_object.news_process()
    return news_object

if __name__ == '__main__':
    # news list
    # run read news
    # run change words
    # run konlpy
    # run counting
    # run filtering
    
    log_start_main = '{} start works - number of cpu : {}, working core : {}'.format(str(datetime.now().strftime('%Y%m%d %H:%M:%S')),
                                                                                       str(os.cpu_count()),
                                                                                       str(os.cpu_count() - 1))
    print(log_start_main)
    start = time.time()
    
    Settings.settings('settings.csv')
    
    news_routes = get_news_file_list(Settings.news_route)
    if news_routes is None:
        print('news 폴더 경로를 확인하십시오.')
        print(Settings.news_route)
        exit()
    
    news_list = []
    for route in news_routes:
        news_list.append(News(route))

        # 멀티
    pool = multiprocessing.Pool(os.cpu_count() - 1)
    news_list = pool.map(run_News, news_list)
    pool.close()
    pool.join()

        # 싱글
#     for news in news_list:
#         news.news_process()

    log_end_main = '{} end works - {} sec.'.format(str(datetime.now().strftime('%Y%m%d %H:%M:%S')),
                                                   str(time.time() - start))
    print(log_end_main)
    
    with open('log_' + str(datetime.now().strftime('%Y%m%d_%Hh-%Mm-%Ss')) +'.txt', 'w', encoding='utf-8') as fw:
        news_log = []
        news_log.append(log_start_main)
        
        for news in news_list:
            item_log = news.process_log
            if item_log == None:
                item_log = 'None'
            news_log.append(item_log)
            
        news_log.append(log_end_main)
        final_log = '\n'.join(news_log)
        
        fw.write(final_log)
