import requests

from bs4 import BeautifulSoup

database=[]

def Data(url):
    Collatecontent=requests.get(url=url).content
    soup=BeautifulSoup(Collatecontent,'html.parser')

    table = soup.find("table",{"class":"table scoretable"})
    th=table.find_all("th")
    tr=table.find_all("td")
    for data in th:
        database.append(data.text)
    for datas in tr:
        database.append(datas.text)
    print(database)
Data(url="http://www.cricmetric.com/ipl/ranks/")
