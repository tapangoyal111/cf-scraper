from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import  xlsxwriter
from readfiles import *
# a=["https://codeforces.com/ratings/organization/2398","https://codeforces.com/ratings/organization/2566","https://codeforces.com/ratings/organization/754","https://codeforces.com/ratings/organization/2397"]
dsec,dfs=create_dick()
contest = 1283
date="(28-12-2019)"
s1 = "http://codeforces.com/contest/" + str(contest) + "/standings/page/"
w = xlsxwriter.Workbook("contest" + str(contest) + date + ".xlsx")
w1 = w.add_worksheet()
w2=w.add_worksheet()
w1.write(0, 0, "Rank")
w1.write(0, 1, "Name")
w1.write(0, 2, "Branch")
w1.write(0, 3, "Institute Id")
w1.write(0, 4, "Handle")
w2.write(0, 0, "Rank")
w2.write(0, 1, "Name")
w2.write(0, 2, "Branch")
w2.write(0, 3, "Institute Id")
w2.write(0, 4, "Handle")

row1 = 1
row2=1
rows_per_page=200
for i in range(1,10000//rows_per_page):
    ucl = ureq(s1 + str(i))
    h = ucl.read()
    ucl.close()
    ht = soup(h, "html.parser")
    ht = ht.findAll("table", {"class": "standings"})[0]
    j = ht.findAll("tr")
    for k in range(1, rows_per_page+1):
        print(k)
        try:
            b = []
            a1 = j[k].findAll("td", {"class": "contestant-cell"})[0]
            a1 = a1.text.strip()
            rank = j[k].findAll("td")[0]
            rank = rank.text.strip()
            print("rank",rank,a1)
            if a1 in dsec:
                w1.write(row1, 0, rank)
                w1.write(row1,1,dsec[a1][0])
                w1.write(row1, 2, dsec[a1][2])
                w1.write(row1, 3, dsec[a1][1])
                w1.write(row1, 4, a1)
                row1+=1
            elif a1 in dfs:
                w2.write(row2, 0, rank)
                w2.write(row2, 1, dfs[a1][0])
                w2.write(row2, 2, dfs[a1][2])
                w2.write(row2, 3, dfs[a1][1])
                w2.write(row2, 4, a1)
                row2 += 1
        except:
            w.close()
            exit()



