from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e: # 서버 작동 확인
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body
    except AttributeError as e: # 태그 존재 확인
        return None
    return title

title = getTitle("https://www.pythonscraping.com/pages/warandpeace.html")
if title == None:
    print("No title found")
else:
    print(title)