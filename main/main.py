#from newsRecoding import recoding
#from newsRefining import refining

from nlp import knlp, count, filter
from newsRefining import refining
from newsRecoding import recoding

import os, time, re
import json, pandas
import itertools
from datetime import datetime
import multiprocessing


debug_log = ''

def get_debug_string(txt):
    return ' '.join([str(datetime.now().strftime('[%Y%m%d] [%H:%M:%S]')), txt+'\n'])

def add_log(txt, prefix = True):
    global debug_log
    if prefix:
        debug_log += get_debug_string(txt)
    else:
        debug_log += txt + '\n'
    
def print_log(txt):
    add_log(txt)
    print( txt )

def get_filename(news_route):
    return news_route.split('\\')[-1].split('.')[0]

def get_news_file_list(folder_route):
    if os.path.isdir(folder_route) == False:
        return None
    
    news_pattern = re.compile('.*news_[\d]+.json$')
    file_list = []
    for file in os.listdir(folder_route):
        file_route = folder_route + '\\' + file
        
        if os.path.isfile(file_route):
            if news_pattern.match(file_route) != None:
                file_list.append(file_route)
                
        elif os.path.isdir(file_route):
            file_list.extend(get_news_file_list(file_route + '\\'))
    
    return file_list

class Settings():
    news_route = None
    konlp_class = None
    konlp_function = None
    filter_route = None
    result_route = None
    user_dict_route = None
    recoding_dict_route = None
    
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
        cls.user_dict_route = settings.user_dictionary[0].replace('\u202a','')
        cls.recoding_dict_route = settings.recoding_dictionary[0].replace('\u202a','')

class News():
    def __init__(self, news_route):
        self.route = news_route
        self.name = get_filename(news_route)
        self.news = None
        self.nouns = None
        self.counts = None
        self.result = None
        self.process_log = None
        
    def write_csv(self, data, route = None, modifier = ''):
        if data is None:
            print('{} in empty.', data.__name__)
            return
        
        if route is None:
            route = ''
        
        if os.path.isdir(route) == False:
            os.makedirs(route, exist_ok = True)
        
        route = route + '\\'
        
        filename = route + '{}_{}.csv'.format(self.name, modifier)
        data.to_csv(filename, sep = ',', index = False, encoding='cp949')
        
    def write_nouns(self, route = None):
        if self.nouns is None:
            print('nouns is empty.')
            return
        
        if route is None:
            route = ''
        if os.path.isdir(route) == False:
            os.makedirs(route, exist_ok = True)
        
        route = route + '\\'
            
        filename = route + '{}_{}.csv'.format(self.name, 'nouns')
        with open(filename, 'w', encoding='cp949') as fw:
            fw.write('\n'.join(self.nouns))
    
    def get_news_debug_string(self, txt):
        return get_debug_string(' '.join(['os{} : {}'.format(os.getpid(), self.name), txt]))
    
    def news_process(self):
        Settings.settings(r'../files/settings.csv')

        # refine
        start_refine_news = time.time()
        refine_data = refining.refin_new_day(self.route)
        refine_data = json.dumps(refine_data)
        end_refine_news = time.time()

        log_refine_news = self.get_news_debug_string('- refine - {}'.format(str(end_refine_news - start_refine_news)))
        print(log_refine_news)
        
        # recoding
        start_recoding_news = time.time()
        recode_dict = recoding.load_recode_dict(Settings.recoding_dict_route)
        recoding_data = recoding.replace_all(recode_dict, refine_data)
        #data = knlp.read_news(newsroute = self.route)
        self.news = knlp.read_news(newsdata = recoding_data)
        end_recoding_news = time.time()
        
        log_recoding_news = self.get_news_debug_string('- recoding - {}'.format(str(end_recoding_news - start_recoding_news)))
        print(log_recoding_news)

#         self.news = knlp.read_news(self.route)
#         end_read_news = time.time()
#         
#         log_read_news = 'os{} : {} - read_news() - {}'.format(os.getpid(),
#                                                             self.name,
#                                                             str(end_read_news - start_read_news))
#         print(log_read_news)
        
        # konlp
        start_konlpy = time.time()
        self.nouns = knlp.get_KoNLP(self.news,
                                    Settings.konlp_class,
                                    Settings.konlp_function,
                                    userDict = Settings.user_dict_route)

        self.nouns = list(itertools.chain.from_iterable(self.nouns))
        end_konlp = time.time()
        
        log_nouns = self.get_news_debug_string('- cTwitter.nouns - {}'.format(str(end_konlp - start_konlpy)))
        print(log_nouns)
        self.write_nouns(Settings.result_route + '_nouns')

        # count
        start_count = time.time()
        count_data = count.get_unique_count(self.nouns)
        self.counts = pandas.DataFrame({'word':list(count_data.keys()), 'count':list(count_data.values())})
        self.counts = self.counts.sort_index(axis = 1, ascending  = False)
        end_count = time.time()
        
        log_count = self.get_news_debug_string('- count - {}'.format(str(end_count - start_count)))
        print(log_count)
        
        # filter
        start_filter = time.time()
        self.result = filter.filter_count(self.counts, Settings.filter_route)
        end_filter = time.time()
        
        log_filter = self.get_news_debug_string('- filter - {}'.format(str(end_filter - start_filter)))
        print(log_filter)
        
        # save log
        self.process_log = ''.join([log_refine_news, log_recoding_news, log_nouns, log_count, log_filter])
        
        # save result
        self.write_csv(self.result, Settings.result_route, modifier='result')

def run_News(news_object):
    if news_object is None:
        return None
    
    news_object.news_process()
    return news_object
        
def process_refine(news_route_list):
    news_refine = []
    for news_route in news_route_list:
        refine_data = refining.refin_new_day(news_route)
        if refine_data is not None and len(refine_data) > 0:
            news_refine.append(refine_data)
    
    if news_refine is None:
        print_log('refine result is None. please check refine process or check news directory.')
        return None
    
    return news_refine

def process_recoding(news_list):
    print(Settings.recoding_dict_route)
    recode_dict = recoding.load_recode_dict(Settings.recoding_dict_route)
    recode_list = []
    for news_data in news_list:
        news_data = json.dumps(news_data)
        recode_list.append(recoding.replace_all(recode_dict, news_data))
    
    return recode_list

def write_json(words, json_name, result_directory):
    if os.path.isdir(result_directory) == False:
        os.makedirs(result_directory, exist_ok=True)

    new_name = result_directory + '\\re_' + json_name

    file = open(new_name,'w',encoding='utf-8')
    json.dump(words, file, ensure_ascii = False,indent = 1)

def split_news_routes(news_routes, split_unit=100):
    result = []
    route_length = len(news_routes)
    for i in range(0, int( route_length/split_unit ) + 1):
        result.append(news_routes[ i*split_unit : min((i+1) * split_unit, route_length)])
    return result

def main():
    log_start_main = 'start works - number of cpu : {}, working core : {}'.format(str(os.cpu_count()),
                                                                                  str(os.cpu_count() - 1))
    print_log(log_start_main)
    start = time.time()
    
    settings_route = r'../files/settings.csv'
    Settings.settings(settings_route)
    
#     Settings.settings(settings_route)
#     news_list = konlp.get_news_file_list(konlp.Settings.news_route)
#     
#     if news_list is None or len(news_list) == 0:
#         print("news directory in empty. check settings.csv's news_route")
#         return
#     start_refine = time.time()
#     news_refine_list = process_refine(news_list)
#     print('finished work - refine, time :', time.time() - start_refine)
#     print('length of refine list :', len(news_refine_list))
#     
#     start_recoding = time.time()
#     news_recoding_list = process_recoding(news_refine_list)
#     print('finished work - recoding, time :', time.time() - start_recoding)
#     print('length of recode list :', len(news_recoding_list))
    
    news_routes = get_news_file_list(Settings.news_route)
    news_routes = split_news_routes(news_routes, 200)
    if news_routes is None or len(news_routes) == 0:
        print_log("news directory in empty. check settings.csv's news_route.")
        print_log(Settings.news_route)
        return
            
    news_list = []
    for routes in news_routes:
        temp_news_list = []
        for route in routes:
            temp_news_list.append(News(route))
    
            # 멀티
        pool = multiprocessing.Pool(os.cpu_count() - 1)
        news_list.extend(pool.map(run_News, temp_news_list))
        pool.close()
        pool.join()
    
    for news in news_list:
        news_log = news.process_log
        if news_log == None:
            news_log = 'None'
        add_log(news_log, prefix=False)
    
    log_end_main = 'end works - {} sec.'.format(str(time.time() - start))
    print_log(log_end_main)
    
    if len(debug_log) > 0:
        with open('log_' + str(datetime.now().strftime('%Y%m%d_%Hh-%Mm-%Ss')) +'.txt', 'w', encoding='utf-8') as fw:         
            fw.write(debug_log)

    
if __name__ == '__main__':    
    main()
    
    