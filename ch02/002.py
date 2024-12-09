from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')

# 자식(children) : 항상 부모보다 한 태그 아래 있음
# 자손(descendants) : 조상보다 몇 태그 아래에 있을 수 있음
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)
print("==========================================")

# 형제
# next_siblings : 테이블에서 데이터 쉽게 수집 가능
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
print("==========================================")

# 부모
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"})
      .parent.previous_sibling.get_text())