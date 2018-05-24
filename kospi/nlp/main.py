# This Python file uses the following encoding: utf-8

from nlp import knlp, count, filter

import os
import re
import pandas
import time

import itertools
import multiprocessing

def get_settings(settings_route):
    df = pandas.read_csv('settings.csv', header = None)
    trans_df = df.transpose()
    settings = trans_df.rename(columns=df[:][0]).drop(0).reset_index(drop=True)

    return settings

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
        print('os{} : {} - Twitter.nouns() - {}'.format(os.getpid(),
                                                        self.name,
                                                        str(end_konlp - start_konlpy)))

        start_count = time.time()
        count_data = count.get_unique_count(self.nouns)
        self.counts = pandas.DataFrame({'word':list(count_data.keys()), 'count':list(count_data.values())})
        self.counts = self.counts.sort_index(axis = 1, ascending  = False)
        end_count = time.time()
        print('os{} : {} - count.get_unique_count() - {}'.format(os.getpid(),
                                                                 self.name,
                                                                 str(end_count - start_count)))
        
        start_filter = time.time()
        self.result = filter.filter_count(self.counts, Settings.filter_route)
        end_filter = time.time()
        print('os{} : {} - filter.filter_count() - {}'.format(os.getpid(),
                                                              self.name,
                                                              str(end_filter - start_filter)))
        
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

if __name__ == '__main__':
    # news list
    # run read news
    # run change words
    # run konlpy
    # run counting
    # run filtering
    
    print('start works - number of cpu :', os.cpu_count())
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

    pool = multiprocessing.Pool(os.cpu_count() - 1)
    pool.map(run_News, news_list)
    pool.close()
    pool.join()


#     i = 0
#     for news in news_list:
#         i += 1
#         start_read_news = time.time()
#         news.news = knlp.read_news(news.route)
#         end_read_news = time.time()
#         print('{} - read_news() - {}'.format(news.name, str(end_read_news - start_read_news)))
#          
#         start_konlpy = time.time()
#         news.nouns = knlp.get_KoNLP(news.news, Settings.konlp_class, Settings.konlp_function)
#         news.nouns = list(itertools.chain.from_iterable(news.nouns))
#         end_konlp = time.time()
#         print('{} - Twitter.nouns() - {}'.format(news.name, str(end_konlp - start_konlpy)))
# 
#         start_count = time.time()
#         count_data = count.get_unique_count(news.nouns)
#         news.counts = pandas.DataFrame({'word':list(count_data.keys()), 'count':list(count_data.values())})
#         news.counts = news.counts.sort_index(axis = 1, ascending  = False)
#         end_count = time.time()
#         print('{} - count.get_unique_count() - {}'.format(news.name, str(end_count - start_count)))
#          
#         start_filter = time.time()
#         news.result = filter.filter_count(news.counts, Settings.filter_route)
#         print(news.result.head())
#         end_filter = time.time()
#         print('{} - filter.filter_count() - {}'.format(news.name, str(end_filter - start_filter)))
#          
#         news.write_result(Settings.result_route)

    print('end works - {} sec.'.format(str(time.time() - start)))
