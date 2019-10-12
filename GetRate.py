import requests
from bs4 import BeautifulSoup


def GetRate(url):
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    response = requests.get(url, headers=user_agent)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, 'lxml')
    ShopFrame = soup.findAll("div", {"class":"list-rst__wrap js-open-new-window"})

    i=0
    while i < len(ShopFrame):
        try:
            #お店の名前を抽出
            ShopName = BeautifulSoup(str(ShopFrame[i].findAll("a", {"class":"list-rst__rst-name-target cpy-rst-name"})[0]), 'lxml').findAll("a", {"class":"list-rst__rst-name-target cpy-rst-name"})[0].getText()
            #お店の評価点を抽出
            ShopRate = BeautifulSoup(str(ShopFrame[i].findAll("span", {"class":"c-rating__val c-rating__val--strong list-rst__rating-val"})[0]), 'lxml').findAll("span", {"class":"c-rating__val c-rating__val--strong list-rst__rating-val"})[0].getText()
            #お店のレビュー件数を抽出
            Rnum = BeautifulSoup(str(ShopFrame[i].findAll("em", {"class":"list-rst__rvw-count-num cpy-review-count"})[0]), 'lxml').findAll("em", {"class":"list-rst__rvw-count-num cpy-review-count"})[0].getText()
            res = '"' + ShopName + '",' + ShopRate + ',' + Rnum + '\n'
            print(res)
            f = open("res.txt", "a", encoding='UTF-8')
            f.write(res)
            f.flush()
        except IndexError:
            #評価点が無かったりスクレイピングできなかったら何もしない
            pass
        i=i+1


def main():
    i = 1
    url=[]
    while i < 61:  #食べログの検索ページは最大60ページまでしか表示できない
        url.append('https://tabelog.com/tokyo/A1301/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1302/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1303/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1304/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1305/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1306/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1307/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1308/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1309/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1310/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1311/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1312/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1313/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1314/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1315/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1316/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1317/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1318/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1319/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1320/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1321/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1322/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1323/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1324/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1325/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1326/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1327/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1328/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1329/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1330/rstLst/' + str(i) + '/')
        url.append('https://tabelog.com/tokyo/A1331/rstLst/' + str(i) + '/')
        for u in url:
            GetRate(u)
        i=i+1

if __name__ == "__main__":
    main() 

