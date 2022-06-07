import requests
# res = requests.get('https://google.com')
res = requests.get('http://nadocoding.tistory.com')
res.raise_for_status () # 응답코드가 정상이 아니면 프로그램 종료

# print('응답코드 :', res.status_code) # 200 이면 정상

print(len(res.text))
print(res.text)

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)