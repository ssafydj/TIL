import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

# 요청 보내서 html 파일 받고 
html = requests.get(url).text


# 뷰숲으로 정제
soup = BeautifulSoup(html, 'html.parser') #뷰숲 고유의 문법


# select 메서드로 list 얻기
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')


# 뽑은 list를 with 구문으로 작성(txt)

with open('example.txt', 'w', encoding = 'utf-8') as f: 
#encoding = 'utf-8' > 한글을 잘 구현되도록
    for name in names:
        f.write(f'{name.text}\n')

# 이 경우엔 순서를 나타내는 rank 함수를 쓰는게 좋을듯...

# 변수 이름(Variable name) > 누구나 직관적으로 의미를 파악할 수 있도록 고민.

