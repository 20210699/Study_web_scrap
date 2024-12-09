# find(), findAll() 함수 예제

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'html.parser')

nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text()) # get_text() : html 태그를 제거하고 텍스트만 출력

# findAll(name, attrs, recursive, string, limit, keywords)
# find(tag, attrs, recursive, string, keywords)
# attrs : 속성으로 이루어진 파이썬 딕셔너리를 받음. 그 중 하나의 일치하는 태그를 찾음.
# recursive (boolean) : true이면 매개변수에 일치하는 태그를 찾아 깊이 들어감.

# string : 찾으려는 텍스트 입력
nameList = bsObj.findAll(string = "the prince")
print(len(nameList))

# keywords : 특정 속성이 포함된 태그를 선택할 때 사용
allText = bsObj.findAll(id = "text")
print(allText[0].get_text())
