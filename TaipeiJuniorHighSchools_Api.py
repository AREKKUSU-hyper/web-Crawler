import urllib.request as req
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=a1c35319-c67d-4c7b-86fe-442874cb3d79"
with req.urlopen(src) as response:
    data=json.load(response)

schoollist=data["result"]["results"]
with open("school.txt", mode="w", encoding="utf-8") as file:
    for school in schoollist:
        file.write(school["school_name"]+": "+school["address"]+"\n")
