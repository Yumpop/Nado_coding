# user agent 사용해도 안 됨
import requests
import re
from bs4 import BeautifulSoup

url  = 'http://couqang.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
res = requests.get(url,  headers = headers)
# print('응답코드 :', res.status_code) # 200 이면 정상
print(res.status_code)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, 'lxml')

# print(res.text)
# items = soup.find_all('li', attrs = {'class' : re.compile('^search-product')})
# print(items[0].find('div', attrs = {'class' : 'name'}).get_text())

