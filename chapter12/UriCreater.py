import requests
from bs4 import BeautifulSoup

class Creater:
          #https://cd.lianjia.com/chengjiao/pg2ng1hu1nb1l3/
    url = "https://cd.lianjia.com/chengjiao/ng1hu1nb1l3/"
    uriArray = ["https://cd.lianjia.com/chengjiao/ng1hu1nb1l3/"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

    def __init__(self):
        session = requests.Session()
        req = session.get(Creater.url, headers=Creater.headers)
        bsObj = BeautifulSoup(req.text, "html.parser")
        page = bsObj.find("div", class_="page-box house-lst-page-box").attrs["page-data"]
        pagedict = eval(page)
        print(page)
        self.totolpage = pagedict['totalPage']
        self.currentpage = pagedict['curPage']
        for i in range(self.currentpage, self.totolpage + 1):
            self.uriArray.append("https://cd.lianjia.com/chengjiao/pg" + str(i) + "ng1hu1nb1l3/")
        for listss in list(set(self.uriArray)):
            print(listss)

    def getUriList(self):
        return self.uriArray



if __name__=='__main__':
    creater = Creater()
    creater.getUriList()
