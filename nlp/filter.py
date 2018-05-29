# after Noun

import pandas
import time
import re

# nouns 파일을 읽고 명사 리스트 리턴
def read_nouns_txt(nouns_route):
    with open(nouns_route, 'r', encoding='utf-8') as f:
        data = f.read()
        pattern = re.compile('[\w]+')
        data = pattern.findall(data)
        return data

# def run_filter():
#     name = 'filter_dictionary.xlsx'
#     filter_count(pandas.read_csv('news_20180113_Twitter_count.csv', sep = '\t'), name)

# nouns 에 대한 필터링
# 180529 미사용
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
    
    with open('filtering_delete_word.txt', 'w', encoding = 'utf-8') as fw:
        fw.write(delete_words)

# 빈도수 추출된 데이터에 대한 필터링
def filter_count(counts, filtername):
    # pandas.read_excel()을 하려면 xlrd 패키지를 설치해야 한다.
    filter_dictionary = pandas.read_excel(filtername, usecols=0)
    counts = counts.dropna()
    
    filter_set = set(filter_dictionary.word)   
    words_set = set(counts.word)
    
    result_set = words_set.difference(filter_set)
    
    filter_series = counts.word.isin(result_set)
    remove_indices = filter_series.index[filter_series == False].tolist()
    
    remove_indices = sorted(remove_indices, reverse = True)
    counts = counts.drop(index = remove_indices)
        
    return counts

if __name__ == '__main__':
    pass


