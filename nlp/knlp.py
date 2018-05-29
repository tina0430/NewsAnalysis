from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter
from konlpy.tag import Hannanum

from ckonlpy.tag import Twitter as cTwitter

import time
import json
import re
import pandas

from itertools import chain

# 문단을 문장으로 분할
def split_paragraph(paragraph):
    pt = re.compile(r'[가-힣]\.')
    start_idx = 0
    sentences = []

    while True:
        end_idx = pt.search(paragraph[start_idx:])
        if end_idx == None or start_idx >= len(paragraph):
            break
        
        end_idx = end_idx.end() + start_idx
        sentences.append(paragraph[start_idx:end_idx].strip())
        start_idx = end_idx

    if len(sentences) == 0:
        sentences.append(paragraph)
        
    return sentences

# nouns 결과물에 대한 출력 함수
def write_list(data, fileobj):
    for i, line in enumerate(data):
        i += 1
        fileobj.write(line)
        if i % 5 == 0:
            fileobj.write('\n')
        else:
            fileobj.write('\t')
    fileobj.write('\n')

# pos 결과물에 대한 출력 함수
def write_pos(pos_data, fileobj, sep = '_:_'):
    for i, line in enumerate(pos_data):
        i += 1
        txt = ''
        for j, cell in enumerate(line):
            if j == 0:
                txt = txt + '%s' %cell
            else:
                txt = txt + sep + '%s'%cell

        if i % 5 == 0:
            txt = txt + '\n'
        else:
            txt = txt + '\t'
        fileobj.write(txt)

# newsroute = 뉴스 경로
# newsdata = 뉴스 json (dict) 객체
def read_news(sep='\n', *args, **kwds):
    newsroute = kwds.get('newsroute')
    newsdata = kwds.get('newsdata')

    jdata = None
    if newsroute is not None:
        with open(newsroute, 'r', encoding='utf-8') as f:
            jdata = json.loads(f.read())
    elif newsdata is not None:
        jdata = newsdata

    news_lines = []
    for i in range(len(jdata)):
        news_idx = 'news' + str(i + 1)
        news_lines.append(jdata[news_idx]['title'])
        news_lines.append(jdata[news_idx]['contents'])
    news = sep.join(news_lines)
    return news

# text : 형태소 분석을 수행할 문자열
# konlp_name : 형태소 분석 태그(엔진) 클래스 이름
# func_name : 형태소 분석에 사용할 함수 이름
# userDict : 사용자 정의 사전
def get_KoNLP(text, konlp_name, func_name, **kwds):
    classname = globals()[konlp_name]
    konlp_obj = classname()
    
    # 사용자 정의 사전 경로
    userDict_name = kwds.get('userDict')
    if userDict_name is not None:
        if konlp_name == 'cTwitter':
            userdict = pandas.read_csv(userDict_name, encoding = 'utf-8', header = None)
            konlp_obj.add_dictionary(userdict[0].tolist(), 'Noun')

    konlp_func = getattr(konlp_obj, func_name)
    
    text = text.strip().split('\n')

    #print("KoNLPY Engine : {}, use function : {}, start".format(konlp_name, func_name))
    #start_time = time.time()
    
    words = []
    for data in text:
        words.append(konlp_func(data))

    #end_time = time.time()
    #print('%s %s end - %s sec' % (konlp_name, func_name, str(end_time - start_time)) )
    
    return words


# 180529 main에서 사용하지 않음. 테스트용.
# KoNLP를 실행하고 결과를 리턴합니다.
# news_route : 크롤링한 뉴스 파일 경로
# nlp_obj : KoNLP 객체 - Twitter, Kkma, Komoran, Hannanum 등
# bMorphs, bNouns, bPos : morphs(), nouns(), pos() 함수 의 실행 여부
# bWriteTxT : 결과를 파일로 출력할 것인지 여부
def run_KoNLP(news_data, nlp_obj, bMorphs = False, bNouns = False, bPos = False, bWriteTxT = True):
    data = read_news(news_data)
    class_name = nlp_obj.__class__.__name__
    
    nlp_func = []
    write_func = []
    titles = []
    if bMorphs:
        titles.append(class_name + '_morphs\n')
        nlp_func.append(nlp_obj.morphs)
        write_func.append(write_list)
        
    if bNouns:
        titles.append(class_name + '_nouns\n')
        nlp_func.append(nlp_obj.nouns)
        write_func.append(write_list)
        
    if bPos:
        titles.append(class_name + '_pos\n')
        nlp_func.append(nlp_obj.pos)
        write_func.append(write_pos)
    
    nlp_results = []
    data_split = data.split('\n')
    
    print(class_name, '시작')
    start_time = time.time()
    for i in range(len(titles)):
        words = []
        for data in data_split:
            words.append(nlp_func[i](data))
        nlp_results.append(words)
    end_time = time.time()
    print(class_name, '끝 - %s 초' % str(end_time - start_time) )

    if bWriteTxT:
        # '~/news20180101.json'.split('\\')[-1] : news20180101.json
        # 'news20180101.json'.split('.')[0] : news20180101
        knlp_filename = '{}_{}.txt'.format(news_data.split('\\')[-1].split('.')[0],
                                           class_name)
        with open(knlp_filename, 'w', encoding = 'utf-8') as fstream:
            for i in range(len(titles)):
                fstream.write(titles[i])
                nlp_words = list(chain.from_iterable(nlp_results[i]))
                write_func[i](nlp_words, fstream)

def run_kkma(data):
    kkma = Kkma()
    start_time = time.time()
    print('kkma 시작')
    kkma_morphs = kkma.morphs(data)
    kkma_nouns = kkma.nouns(data)
    kkma_pos = kkma.pos(data)
    end_time = time.time()
    print('kkma 끝 - %s 초' % str(end_time - start_time) )
    kkma_sentences = kkma.sentences(data)
    
    with open('kkma.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('kkma time : %s s\n' % str(end_time - start_time) )
        fstream.write('kkma_morphs\n')
        write_list(kkma_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_nouns\n')
        write_list(kkma_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_pos\n')
        write_pos(kkma_pos, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_sentences\n')
        write_list(kkma_sentences, fstream)
        fstream.write('\n')


if __name__ == '__main__':
    pass
    #news_route = 'news_20180113.json'
    
    #run_KoNLP(news_route, Twitter(), bNouns = True)
#     run_KoNLP(news_route, Komoran(), bNouns = True)
#     run_KoNLP(news_route, Hannanum(), bNouns = True)
#     run_KoNLP(news_route, Kkma(), bNouns = True)
#     text = '우리나라는 아시아에 있다. 잠을 세시간밖에 자지 못했다.\n공사장 소리가 시끄럽다. 하지만 어떻게 할 수가 없다.\n그런데 지금 이게 뭘 하는 것인지 모르겠다. 난 무엇을 쓰고있는 것인가. 배가 고프지 않다. 그런데 점심은 먹어야 한다.\n살어리 살어리랐다. 청산에 살어리랐다.\n'
#     
#     start = time.time()
#     #print( get_KoNLP(text, 'Twitter', 'nouns') )
#     print("job's done :", str(time.time() - start))
