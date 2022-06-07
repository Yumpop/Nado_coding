# user gaent는 브라우저마다 다름 
# 구글에 user agent string 치면 내 user agent나옴
import requests 

url = 'https://nadocoding.tistory.com'
headers = {'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
res = requests.get(url)
res.raise_for_status () # 응답코드가 정상이 아니면 프로그램 종료

with open('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)