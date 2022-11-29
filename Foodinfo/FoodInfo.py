# this program webcrawls specific nutritions on the food you want
# https://consumer.fda.gov.tw/Food/TFND.aspx?nodeID=178&k=%E8%8A%8B%E9%A0%AD

import requests
from bs4 import BeautifulSoup
while True:
    print("停止搜尋輸入 X")
    url = input("複製你想知道成分的網址，貼上在這裡: ")
    if url == "X":
        break
    r = requests.get(url)
    # this will get the html of the web
    # print(r.text)

    html = BeautifulSoup(r.text, 'html.parser')
    # all the ingredients has 8 columns
    Ingredients = html.find_all('td', class_="txt_C")
    nutritions = []
    print("輸入你想知道的東西的含量，字一定要對，如果要停止輸入了，輸入 X")
    while True:
        tmp = input("你想知道的東西含量: ")
        if tmp=="X":
            break
        nutritions.append(tmp)
    contains = [""]*len(nutritions)
    units = [""]*len(nutritions)
    for i in range(int(len(Ingredients)/8)):
        if "" not in units:
            break
        for j in range(len(nutritions)):
            if nutritions[j] in Ingredients[i*8+1]:
                tmp = str(Ingredients[i*8+2])
                units[j] = tmp[31:len(tmp)-5]
                tmp = str(Ingredients[i*8+3])
                if tmp[36:len(tmp)-5]=='':
                    contains[j] = 0
                else:
                    contains[j] = float(tmp[36:len(tmp)-5])

    for i in range(len(nutritions)):
        print(nutritions[i]+": "+str(contains[i])+" "+units[i])