import re

from collections import Counter
from operator import itemgetter

def read_nouns(filename):
    with open(filename, 'r', encoding = 'utf-8') as fstream:
        data_list = []
        flag_find_nouns = False
        while True:
            line = fstream.readline()
            
            if flag_find_nouns == False or len(re.findall(r'[.]*nouns[.]*', line)) > 0:
                flag_find_nouns = True
                continue
            
            if not line:
                break;
            line = line.replace('\n', '')
            line = line.split('\t')
            for data in line:
                data_list.append(data)
    
    return data_list
            
def write_count_data(filename, count_data):
    with open(filename, 'w', encoding = 'utf8') as fstream:
        for key, value in count_data.items():
            fstream.write(key + '\t' + str(value) + '\n')

def get_unique_count(data):
    count_data = Counter(data)
    sort_data = dict( sorted(count_data.items(), key = itemgetter(1), reverse = True) )
    return sort_data
        
if __name__ == '__main__':
    read_filename = 'twitter.txt'
    write_filename = 'twitter_count.txt'
    # 읽을 파일 - nouns 부터 읽는다.
    data = read_nouns(read_filename)
    # 빈도 수를 구하고 내림차순 정렬
    count_data = get_unique_count(data)
    # 내보내질 파일
    write_count_data(write_filename, count_data)
    