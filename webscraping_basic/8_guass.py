#https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 에서 더 공부할 수 있음

from array import array
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all('td', attrs= {'class' : 'title'}) 
# print(title)
# print('https://comic.naver.com' + link)

# 웹툰 이름과 링크 가져오기 
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'https://comic.naver.com' + cartoon.a['href']
#     print(title, link)

# 웹툰 평균평점 계산
total_rate = 0
cartoons = soup.find_all('div', attrs={'class' : 'rating_type'})

for cartoon in cartoons:
    score = cartoon.find('strong').get_text()
    print(score)
    total_rate += float(score)
print('전체점수 :', total_rate)
print('평균점수 :', total_rate/len(cartoons))
