from bs4 import BeautifulSoup

import urllib.request as urlreq
import urllib.parse as urlparser

import datetime

import pandas
import re

# 날짜 형식 : YYYY/MM/DD
def run_requests(start_date = '2018/04/01', end_date = '2018/05/01'):
    kospi_url = r'https://kr.investing.com/instruments/HistoricalDataAjax'
    
    kospi_header = {'Content-Type':"application/x-www-form-urlencoded",
                    "Cache-Control":"no-cache",
                    "X-Requested-With":"XMLHttpRequest",
                    "Accept":"text/plain",
                    'User-Agent':r'Chrome/66.0.3359.139'}

    body = {'curr_id': 37426,
            'smlID': 2055174,
            'header': urlparser.quote('코스피지수 내역'),
            'st_date': urlparser.quote(start_date),
            'end_date': urlparser.quote(end_date),
            'interval_sec': 'Daily',
            'sort_col': 'date',
            'sort_ord': 'DESC',
            'action': 'historical_data'}

    body = urlparser.urlencode(body)
    body = body.encode('utf-8')
    
    req = urlreq.Request(  url = kospi_url,
                           headers = kospi_header,
                           data = body,
                           method='POST')

    try:
        response = urlreq.urlopen(req)
        if response.getcode() == 200:
            print('[{}] : url request success'.format( datetime.datetime.now() ))
            print('url : {}'.format(req._full_url))
            
            return response.read().decode('utf-8')
    except Exception as err:
        print('[{}] : url request failed'.format( datetime.datetime.now() ))
        print( 'error for url : {}'.format(req._full_url))
        print(err)
        return None

# 날짜 형식 : YYYY/MM/DD
# toCSV : 읽어온 데이터를 csv 로 저장합니까?
# col_kor : 컬럼명을 한글로 설정합니까? True : 한글, False : 영문
# pandas.DataFrame 리턴.
def get_kospi(start_date = '2018/04/01', end_date = '2018/05/01', col_kor = True, toCSV = False):
    data = run_requests(start_date, end_date)
    soup = BeautifulSoup(data, 'html.parser')
    
    # 영문 컬럼
    head_eng = []
    # 한글 컬럼
    head_kor = []
    # 데이터 행
    data_list = []
    # 맨 마지막의 요약 수치
    kospi_result = []

    curr_table = soup.find('table', {'id':'curr_table'})
    thead = curr_table.find('thead')
    ths = thead.find_all('th')

    for th in ths:
        head_eng.append(th.attrs.get('data-col-name'))
        head_kor.append(th.text.replace(' ', ''))
    
    pattern = re.compile(r'[가-힣%,]+')
    
    tbody = curr_table.find('tbody')
    tr_list = tbody.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) == 0:
            continue
        
        row = []
        for i, td in enumerate(td_list):
            cell = None
            if i == 5:
                # 거래량 은 data-real-value 속성의 값을 취한다.
                cell = td.attrs.get('data-real-value')
                #row.append(td.attrs.get('data-real-value'))
            else:
                cell = td.text.replace(' ', '')
                #row.append(td.text.replace(' ', ''))
            
            cell = pattern.sub('', cell)
            if i == 5:
                cell = int(cell)
            elif i >= 1:
                cell = float(cell)
                
            row.append(cell)

        data_list.append(row)
        
    result_table = soup.find('table', {'id':'placehereresult2'})
    for data in result_table.find_all('td'):
        kospi_result.append(data.text.replace(' ', ''))

    columns = None
    if col_kor == True:
        columns = head_kor
    else:
        columns = head_eng
        
    data_list.reverse()
    kospi_df = pandas.DataFrame(data = data_list, columns = columns)
    
    if toCSV == True:
        filename = start_date.replace(r'/', '') + '_' + end_date.replace(r'/', '') + '_' + 'kospi.csv'
        kospi_df.to_csv(filename, header = True, index = False, encoding = 'utf-8')
        
    return kospi_df

if __name__ == '__main__':
    start = '2018/05/01'
    end = '2018/05/10'
 
    # inversting 사이트에서 kospi 지수를 얻어옵니다.
    # toCSV = True : 20180101_20180501_kospi.csv 형식으로 저장합니다.
    kospi_df = get_kospi(start, end, toCSV = True)
    print(kospi_df)
     
    # csv를 읽어옵니다.
    filename = start.replace(r'/', '') + '_' + end.replace(r'/', '') + '_' + 'kospi.csv'
    read_df = pandas.read_csv(filename, header=0, encoding='utf-8')
    print(read_df)
    