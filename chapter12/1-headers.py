import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
url = "https://cd.lianjia.com/chengjiao/pg2c3011056131816/?sug=%E5%8D%8E%E9%98%B3%E6%BB%A8%E6%B2%B3%E8%8A%B1%E5%9B%AD"
req = session.get(url, headers=headers)
#print(req.text)
bsObj = BeautifulSoup(req.text, "html.parser")
print(bsObj.find("div", class_="page-box house-lst-page-box").attrs["page-data"])
