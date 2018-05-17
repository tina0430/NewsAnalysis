import re

from collections import Counter
from operator import itemgetter

# 읽을 파일 - nouns 부터 읽는다.
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

# 내보내질 파일
def write_count_csv(filename, count_data, sep = ','):
    with open(filename, 'w', encoding = 'utf8') as fstream:
        fstream.write('word' + sep + 'count\n')
        for key, value in count_data.items():
            fstream.write(key + sep + str(value) + '\n')

# 빈도 수를 구하고 내림차순 정렬
def get_unique_count(data):
    count_data = Counter(data)
    sort_data = dict( sorted(count_data.items(), key = itemgetter(1), reverse = True) )
    return sort_data

# 파일 경로를 전달
def create_count_csv(read_file_route):
    data = read_nouns(read_file_route)
    count_data = get_unique_count(data)
    
    write_filename = read_file_route.split('\\')[-1].split('.')[0] + '_count.csv'
    write_count_csv(write_filename, count_data)
        
if __name__ == '__main__':
    create_count_csv('news_20180113_Twitter.txt')
    create_count_csv('news_20180113_Hannanum.txt')
    create_count_csv('news_20180113_Komoran.txt')
    