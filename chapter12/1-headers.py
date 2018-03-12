import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
#文路径转换：https://www.cnblogs.com/hannover/p/4657463.html#
url = "https://cd.lianjia.com/chengjiao/pg1c3011056131816/?sug=滨河花园"
uriArray=["https://cd.lianjia.com/chengjiao/pg1c3011056131816/?sug=滨河花园"]
req = session.get(url, headers=headers)
#print(req.text)
bsObj = BeautifulSoup(req.text, "html.parser")
infoList = bsObj.findAll("div", class_="info")
page = bsObj.find("div", class_="page-box house-lst-page-box").attrs["page-data"]
pagedict = eval(page)
print(page)
totolpage = pagedict['totalPage'];
currentpage = pagedict['curPage'];
print(totolpage)
print(currentpage)
for i in range(currentpage,totolpage + 1):
    uriArray.append("https://cd.lianjia.com/chengjiao/pg" + str(i) + "c3011056131816/?sug=滨河花园")


for listss in list(set(uriArray)):
    print(listss)
for info in infoList:
    print(info)
    print(info.find("a").get_text())
    print(info.find("div", class_="dealDate").get_text())
    print(info.find("div", class_="totalPrice").get_text())
    print(info.find("div", class_="unitPrice").get_text())
