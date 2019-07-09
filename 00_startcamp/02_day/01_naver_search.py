import requests
from bs4 import BeautifulSoup 

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')
names = soup.select(#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k)

for name in names: 
print(names.text))
