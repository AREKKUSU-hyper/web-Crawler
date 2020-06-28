from urllib import request as req
from bs4 import BeautifulSoup as bs 

def getData(url): # 把抓取單一頁面的程式包裝
    request=req.Request(url,headers={
                            "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
                            "cookie":'_ga=GA1.2.1446506856.1481296007; __cfduid=d3f4c5e39e68abd99bb3d6ac2fe777c291545875296; over18=1'
                        })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    soup=bs(data,features="html.parser")
    titles=soup.find_all("div",class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)
    # 抓取上一頁的連結
    lastpage=soup.find("a",string="‹ 上頁") # 找到內文是"‹ 上頁"的a標籤
    return lastpage["href"]

# 主程序:抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    print("---------------------------------------------")
    count+=1