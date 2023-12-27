from pydoc import text

import requests
from matplotlib import pyplot as plt
from pandas import *
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

database=[]

def Data(url, clean_currency=None):
    Collatecontent=requests.get(url=url).content
    soup=BeautifulSoup(Collatecontent,'html.parser')

    table = soup.find("table",{"class":"table scoretable"})

    th=table.find_all("th")
    for i in th:
        database.append(i.text)
    df=DataFrame(columns=database)


    body = table.find_all("tr")
    for i in body[1:]:
        player=i.find_all("td")
        playerdata=[tr.text for tr in player]
        #print(playerdata)
        #len is a length
        l=len(df)
        #loc is a location
        df.loc[l]=playerdata

    print(df)
Data(url="http://www.cricmetric.com/ipl/ranks/")
