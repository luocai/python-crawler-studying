# 爬虫原理（流程）
* 发送请求（获取页面）
* 解析页面
* 存储数据

# 笔记
* 请求：
```
import requests
res = requests.get("http://www.xxxx.com")
res.encoding = "utf-8"
```
* 解析：
```
 from bs4 import BeautifulSoup
	html = xxxx
	soup = BeautifulSoup(html, "htmp.parser")
	print(type(soup))
	print(soup.text)

	header = soup.select('h1')
	print(header) // 是一个数组 [<h1 id="title">Hello</h1>]
	print(header[0]) //取出结果  <h1 id="title">Hello</h1>
	print(header[0].text) // Hello

	alink = soup.select('a')
	print(alink) // 一个数组 [<a>xxx</a>,<a>xxx</a>,...]
	for link in alink:  //遍历
		print(link) //获取完整 单个完整链接<a href="www.xxx.com">xxx</a>
		print(link.text) // 获取 xxx
		print(link[href]) 获取href 

	//按照id获取
	alink = soup.select("#title")
	print(alink)

	//按照class获取
	alinks = soup.select(".link")
	for link in alinks:
		print(link)

	//把xxx移除
	strip()
	//对html树状元素的便力
	xxx.contents
	//乱码解决
	response.encoding = 'utf-8' 或者
	text = response.content.decode('utf-8')
```
 * 存储
 ```
from pymongo import MongoClient
client = MongoClient()
songsdb = client.kugou_db.songs
 data = {
            'rank':rank,
            'singer':singer,
            'name':name,
            'time':time
        }
print(rank,singer,name,time)
song_id = songsdb.insert(data)
```
