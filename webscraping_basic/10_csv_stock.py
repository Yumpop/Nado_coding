import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page='
filename = '시가총액 1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline = '') 
# -sig, 한글이 깨져서 excel에 들어갈 때 사용, newlin : 자동으로 줄바꿈을 없애줌 
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
print(type(title))
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    data_row = soup.find('table', attrs={'class' : 'type_2'}).find('tbody').find_all('tr')
    for row in data_row:
        columns = row.find_all('td')
        if len(columns) <= 1: # 의미 없는 데이터 skip - 줄바꿈
            continue
        data = [column.get_text().strip() for column in columns] # strip() - 뛰어쓰기, tab 삭제
        # print(data)
        writer.writerow(data)

