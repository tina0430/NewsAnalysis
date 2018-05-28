# after Noun

import pandas
import time
import re

from nlp.count import write_count_csv as write_count

def read_nouns_txt(nouns_route):
    with open(nouns_route, 'r', encoding='utf-8') as f:
        data = f.read()
        pattern = re.compile('[\w]+')
        data = pattern.findall(data)
        return data

def run_filter():
    name = './kospiCrwaling/nlp/filter_dictionary.xlsx'
    #filter_count(pandas.read_csv('news_20180113_Twitter_count.csv', sep = '\t'), 'filter_dictionary.xlsx')
    filter_count(pandas.read_csv('news_20180113_Twitter_count.csv', sep = '\t'), name)
        
def filter_nouns(filename, filtername):
    # pandas.read_excel()을 하려면 xlrd 패키지를 설치해야 한다.
    filter_dictionary = pandas.read_excel(filtername, usecols=0)
    nouns = read_nouns_txt(filename)

    remove_indices = []
    
    start_time = time.time()
    for word in filter_dictionary.word:
        print(word)
        for idx, noun in enumerate(nouns):
            if idx not in remove_indices and noun == word:
                remove_indices.append(idx)
            
    print(len(nouns), len(remove_indices))
    remove_indices = sorted(remove_indices, reverse = True)
    delete_words = ''
    for idx in remove_indices:
        delete_words += nouns[idx] + '\n'
        del nouns[idx]

    print('time : %s sec'% str(time.time() - start_time))
    
#     with open('filtering_result.txt', 'w', encoding = 'utf-8') as fw:
#         write_string = ''
#         for i, noun in enumerate(nouns):
#             write_string += noun
#              
#             i += 1
#             if i % 5 == 0:
#                 write_string += '\n'
#             else:
#                 write_string += '\t'
#          
#         fw.write(write_string)

    
    with open('filtering_delete_word.txt', 'w', encoding = 'utf-8') as fw:
        fw.write(delete_words)

def filter_count(counts, filtername):
    # pandas.read_excel()을 하려면 xlrd 패키지를 설치해야 한다.
    filter_dictionary = pandas.read_excel(filtername, usecols=0)
    counts = counts.dropna()
#     temp = [0,1,2,3]
#     data = {    'one':[1,2,3,4,2,4],
#             'two':[5,4,3,2,2,3] }
#     df = pandas.DataFrame(data)
#     for d in df.itertuples():
#         print(d, d[0], d.one, d.Index in temp)
    
#     cnt = 1
#     for word in filter_dictionary.word:
#         cnt += 1
#         if cnt % 100 == 0:
#             print(cnt, len(filter_dictionary.word))
#         for counts_row in counts.itertuples():
#             if counts_row.Index not in remove_indices and counts_row.word == word:
#                 remove_indices.append(counts_row.Index)
    
    filter_set = set(filter_dictionary.word)   
    words_set = set(counts.word)
    
    result_set = words_set.difference(filter_set)
    #print(len(result_set))
    
    filter_series = counts.word.isin(result_set)
    remove_indices = filter_series.index[filter_series == False].tolist()
    
    #print(len(counts), len(remove_indices))
    remove_indices = sorted(remove_indices, reverse = True)
    counts = counts.drop(index = remove_indices)
    
#     counts.to_csv('filtering_result_count.txt', sep = '\t', index = False)

#     delete_words = ''
#     for idx in remove_indices:
#         delete_words += counts.word[idx] + '\n'
#     with open('filtering_delete_word_count.txt', 'w', encoding = 'utf-8') as fw:
#         fw.write(delete_words)
        
    return counts

if __name__ == '__main__':
#     process1 = multiprocessing.Process(target = run_filter)
#     process1.start()
#     process1.join()
    run_filter()


