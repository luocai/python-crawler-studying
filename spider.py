import requests
import urllib.request
import os
import re
from bs4 import BeautifulSoup

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        }
BASE_PAGE_URL = "http://www.doutula.com/article/list/?page="
PAGE_URL_LIST = []
for x in range(1,10):
    urlTemp = BASE_PAGE_URL + str(x);
    PAGE_URL_LIST.append(urlTemp)
for pageUrl in PAGE_URL_LIST:
    res = requests.get(pageUrl,headers = headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    pics = soup.select(".list-group-item")
    for pic in pics:
        titleArr = pic.select(".random_title")
        if len(titleArr) > 0:
            title = titleArr[0]
        imgArr = pic.select(".random_article")
        if len(imgArr) > 0:
            imgs = imgArr[0].select('img')
        print(title.contents[0])
        if not os.path.exists("D:/test/" + title.contents[0]) and title.contents[0] != "赞助商广告":
            os.makedirs("D:/test/" + title.contents[0])
        preUrl = "D:/test/" + title.contents[0]
        for img in imgs:
            if img.has_attr("data-original") :
                url = img['data-original']
                #title = img['alt'].replace("?"," ")  #不能做路径
                if "" in img['alt']:
                    title = img['alt'].replace("", "_")
                else:
                    title = re.sub('[\/:*?"<>|]','_',img['alt'])#去掉非法字符
                #title = img['alt'].replace("", "_")
                print(title)
                postfix = url.split(".").pop(); # 获取后缀
                path = os.path.join(preUrl,title + "." + postfix)
                #print(path)
                urllib.request.urlretrieve(url,filename=path)
              #  print(img['alt'],img['data-original'])


