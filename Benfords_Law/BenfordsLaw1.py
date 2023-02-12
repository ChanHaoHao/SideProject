# Try to test the Benfords Law with python random
# The results seems not to be affected by Benford's law
# import random

# dataset = {}
# n=0

# for n in range(1, 10):
#     dataset[n]=0

# while (n<1000000):
#     tmp=random.randint(1, 9999)%10
#     dataset[tmp]=dataset.get(tmp, 0)+1
#     n+=1

# for n in range(1, 10):
#     print(dataset[n])

import csv
import matplotlib.pyplot as plt
import numpy as np

cities=["Chaiyi1", "Chaiyi2", "Chuanghua", "Hualian",
        "Jinmen", "Kaoshung", "Keelung", "Lianjiang",
        "Miawli", "Nantou", "NewTaipei", "Pintung", 
        "Punghu", "ShiJu1", "ShiJu2", "Taichung", 
        "Tainan", "Taipei", "Taitung", "Taoyuang",
        "Yilan", "Yunlin"]
cities2=["南投縣", "嘉義市", "嘉義縣", "基隆市", 
         "宜蘭縣", "屏東縣", "彰化縣", "新北市", 
         "新竹市", "新竹縣", "桃園市", "澎湖縣",
         "臺中市", "臺北市", "臺南市", "臺東縣",
         "花蓮縣", "苗栗縣", "連江縣", "金門縣",
         "雲林縣", "高雄市"]

filename="Voting\Hualian.csv"
filename2="Voting\總統-A05-3-候選人得票數一覽表-各村里(宜蘭縣).csv"
counts=[0]*9
# for city in cities:
#     filename=filename[0:7]+city+filename[len(filename)-4::]
#     with open(filename, newline='', encoding="utf-8") as csvfile:
#         index=0
#         spamreader=csv.reader(csvfile, delimiter=',')
#         for row in spamreader:
#             index+=1
#             if index>6:
#                 for i in range(1,4):
#                     counts[int(row[i][0])-1]+=1
#     csvfile.close()

for city in cities2:
    filename2=filename2[0:len(filename2)-8]+city+filename2[len(filename2)-5::]
    with open(filename2, newline='', encoding="utf-8") as csvfile:
        index=0
        spamreader=csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            index+=1
            if index>6 and row[0]=="":
                for i in range(2, 5):
                    counts[int(row[i][0])-1]+=1
    csvfile.close()

sums=sum(counts)
for i in range(9):
    counts[i]/=sums
y=[0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
indexs=np.arange(1,10)
plt.scatter(indexs, y, zorder=3, color="r")
plt.plot(indexs, y, zorder=2, color="r")
plt.bar(indexs, counts, width=0.5, zorder=1, color="b")
plt.xticks(indexs)
plt.xlabel("The first digit of each voting area")
plt.ylabel("Ratio")
plt.legend(["Line of Benford's Law", "Points of Benford's Law", "The result"])
plt.show()
plt.savefig('Taiwan election plot2.png')