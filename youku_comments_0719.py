import requests,re
import codecs
import pymongo
import json
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost',27017)
youku = client['youku']
half_life_0726 = youku['half_life_0726']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
urls = ['http://p.comments.youku.com/ycp/comment/pc/commentList?jsoncallback=n_commentList&app=100-DDwODVkv&objectId=717029520&objectType=1&listType=0&currentPage={}&pageSize=30&sign=30e95b940aa9b665cf30bcf096488451&time=1500630118'.format(str(i)) for i in range(115)]
def comment_parsing (url):
    try:
        wb_data = requests.get(url)
        reg = re.compile(r'"comment":(\[.*?\]),\s*"?totalSize', flags=re.DOTALL)
        x = re.findall(reg,wb_data.text)
        data = json.loads(x[0])
        for item in data:
            print (item)
            half_life_0726.insert_one(item)
    except IndexError:
        print ('ok~')

for url in urls:
    comment_parsing(url)

