import os
os.makedirs("./img/",exist_ok=True)
url="https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

from urllib.request import urlretrieve
urlretrieve(url, "./img/image1.png")

import requests
r=requests.get(url)
with open("./img/image2.png",mode="wb") as file:
    file.write(r.content)

r2=requests.get(url,stream=True) # stream loading
with open("./img/image3.png",mode="wb") as file2:
    for chunk in r2.iter_content(chunk_size=32):
        file2.write(chunk)

