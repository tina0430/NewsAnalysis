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
            
            if flag_find_nouns == False or len(re.findall(r'[.]*_nouns[.]*', line)) > 0:
                flag_find_nouns = True
                continue
            
            if not line:
                break;
            line = line.replace('\n', '')
            line = line.split('\t')
            for data in line:
                data_list.append(data)
    
    return data_list

# _pos 읽기
def read_pos(filename):
    with open(filename, 'r', encoding = 'utf-8') as fstream:
        data_list = []
        flag_find_pos = False
        while True:
            line = fstream.readline()
            
            if flag_find_pos == False or len(re.findall(r'[.]*_pos[.]*', line)) > 0:
                flag_find_pos = True
                continue
            
            if not line:
                break;
            line = line.replace('\n', '')
            line = line.split('\t')
            for data in line:
                data_list.append(data)
    
    return data_list

# 내보내질 파일
# 구분자 = \t (문자열 중 쉼표가 포함된 문자가 있으므로. (ex : 4,000만) )
def write_count_csv(filename, count_data, sep = '\t', bPos = False):
    with open(filename, 'w', encoding = 'utf8') as fstream:
        if bPos:
            fstream.write('word' + sep + 'tag' + sep + 'count\n')

            for key, value in count_data.items():
                key_replace = str(key).replace('_:_', sep)
                fstream.write(key_replace + sep + str(value) + '\n')
        else:
            fstream.write('word' + sep + 'count\n')
            for key, value in count_data.items():
                fstream.write(key + sep + str(value) + '\n')

# 빈도 수를 구하고 내림차순 정렬
def get_unique_count(data):
    count_data = Counter(data)
    sort_data = dict( sorted(count_data.items(), key = itemgetter(1), reverse = True) )
    return sort_data

# 파일 경로를 전달
def create_count_csv(read_file_route, sep = '\t',  bPos = False):
    #data = read_nouns(read_file_route)
    data = read_pos(read_file_route)
    count_data = get_unique_count(data)
    
    write_filename = read_file_route.split('\\')[-1].split('.')[0] + '_count.csv'
    write_count_csv(write_filename, count_data, sep, bPos = bPos)

if __name__ == '__main__':
    pass
    