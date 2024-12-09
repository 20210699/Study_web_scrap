# 정규표현식 사이트 :  https://www.regexpal.com
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re # 정규표현식 임포트

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')
images = bsObj.findAll('img', {"src": re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images: print(image["src"])

# 람다 표현식
soup = bsObj.find(lambda tag: len(tag.attrs) == 2)