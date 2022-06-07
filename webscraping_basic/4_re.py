# 정규식 기본 공부
import re

# ca?e -> 가운데 글자를 모르고 있을 떄 
p = re.compile('ca.e') 
# . (ca.e)  : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)   : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)   : 문자열의 끝 > case , base (O) | face (X)

# print(m.group()) # 매치되지 않으면 에러 발생

def print_match(m):
    if m:
        print('m.group() :', m.group()) # 일치하는 문자열 반환
        print('m.string() :', m.string)  # 입력받는 문자열 반환
        print('m.start() :', m.start()) # 일치하는 문자열의 시작 index
        print('m.end() :', m.end()) # 일치하는 문자열의 끝 index
        print('m.span() :', m.span()) # 일치하는 문자열의 시작 / 끝 index
    else :
        print('매치되지 않음')

# m = p.match('carelsee') # match : 주어진 문자열이 처음부터 일치하는지 확인, 그래서 careless도 match됨
# print_match(m)

# m  = p.search('good care')
# print_match(m)

lst = p.findall('good care cafe') # 일치하는 모든 것을 리스트형태로 반환
print(lst)

# 1. p = re.compile('원하는 형태')
# 2. 