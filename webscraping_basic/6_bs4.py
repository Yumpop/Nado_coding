import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# print(soup.title) 
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음으로 발견되는 a element 출력
# print(soup.a.attrs) # soup 객체에서 처음으로 발견되는 a element 속성들 출력
# print(soup.a['href']) # soup 객체에서 처음으로 발견되는a element 의 href의 속성 '값' 출력

# print(soup.find('a', attrs = {'class' : 'Nbtn_upload'})) # class가 Nbtn_upload 인 a element를 찾기
# print(soup.find(attrs =  {'class' : 'Nbtn_upload'})) # class가 Nbtn_upload인 어떤 element를 찾기 

# print(soup.find('li', attrs = {'class' : 'rank01'}))
# rank1 = soup.find('li', attrs = {'class' : 'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling) # 뒤에 span element가 있음 (개행)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
# rank2 = rank1.find_next_sibling('li') # 뒤에 나오는 형제들중에서 li element를 찾음
# print(rank2.get_text())
# rank1.find_next_siblings('li') # siblings 's'가 붙어서 형제들을 출력

webtoon = soup.find('a', text = '멸망 이후의 세계-제 18 화')
print(webtoon)
