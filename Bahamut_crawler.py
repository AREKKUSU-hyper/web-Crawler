import urllib.request as req
url="https://ani.gamer.com.tw/index.php"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="newanime__content__info")
with open("Anime.txt", mode="w", encoding="utf-8") as file:
    file.write(root.title.string+"\n")
    file.write("---------------------------------------------------------"+"\n")
    for title in titles:
        if title.p !=None:
            if title.span !=None:
                file.write(title.span.string+":"+title.p.string+"\n")

