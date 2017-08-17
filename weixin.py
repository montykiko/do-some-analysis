from bs4 import BeautifulSoup
import requests
import pymongo
from weixin_urls import channel_list

client = pymongo.MongoClient('localhost',27017)
weixin = client['weixin']
half_life = weixin['half_life']

headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}

#单页内容爬取
def page_parsing(url):
    try:
        wb_data = requests.get(url,headers=headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        title = soup.select('div > h2')[0].text.strip()
        time = soup.select('div > em')[0].text
        post_user = soup.select('div > span')[0].text
        articles = soup.select('div div.rich_media_content')
        for article in articles:
            data = {
                'title':title,
                'time':time,
                'post_user':post_user,
                'article':article.get_text()
            }
            print (data)
            half_life.insert_one(data)
    except IndexError:
        print ('ok~')

for url in channel_list.split():
    page_parsing(url)

#age_parsing('http://mp.weixin.qq.com/s?src=3&timestamp=1501049643&ver=1&signature=AgvSYvS0h8yC5Ivb4oBiKQJFl30eWcaFj3ls6FEYVxQVPo1hJqfIvCSRGHFuZYMDoelrblFYh5Kxfy-gIsTFM5pQXxEAsvMBb1N8sjyNlKOy2wOvN22VHp9w21RoE6J2IlHw7Ew*1WRpJwOGj0*DjgXCFDBvZGpCXxHqMJpoVPE=')