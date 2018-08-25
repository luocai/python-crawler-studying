import requests
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
songsdb = client.kugou_db.songs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
BASE_URL = "http://www.kugou.com/yy/rank/home/1-8888.html?from=rank"

def get_info(url):
    res = requests.get(url,headers = headers)

    soup = BeautifulSoup(res.text,'html.parser')

    songs = soup.select(".pc_temp_songlist > ul > li")

    for song in songs:
        rank = song.select(".pc_temp_num")[0].get_text().strip()
        singer = song.select("a")[0].get_text().strip().split('-')[0]
        if singer.endswith("..."):
            name = "未知"
        else:
            name = song.select("a")[0].get_text().strip().split('-')[1]
        time = song.select(".pc_temp_time")[0].get_text().strip()
        data = {
            'rank':rank,
            'singer':singer,
            'name':name,
            'time':time
        }
        print(rank,singer,name,time)
        song_id = songsdb.insert(data)
        print(song_id)
        print("..............................")

if __name__== '__main__':
    urls = ["http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(1)