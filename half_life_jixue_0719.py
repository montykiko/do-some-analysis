import requests,time,re
import pymongo
import json

client = pymongo.MongoClient('localhost',27017)
half_life = client['half_life']
comment = half_life['comment']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Proxy-Connection':'keep-alive'
}

urls = ['http://api-t.iqiyi.com/qx_api/comment/get_video_comments?aid=15394177&albumid=0&categoryid=2&cb=fnsucc&escape=true&is_video_page=true&need_reply=true&need_subject=true&need_total=1&page={}&page_size=10&page_size_reply=3&qitan_comment_type=1&qitancallback=fnsucc&qitanid=15394177&qypid=01010011010000000000&reply_sort=hot&sort=hot&t=0.7062909778193278&tvid=0'.format(str(i)) for i in range(663)]
def comment_parsing(url):
    try:
        wb_data = requests.get(url,headers = headers)
        reg = re.compile(r'"comments":(\[.*?\]),\s*"?count', flags=re.DOTALL)
        x = re.findall(reg,wb_data.text)
        data = json.loads(x[0])
        for item in data :
            print (item)
            comment.insert_one(item)
    except IndexError:
        print ('ok~')

for url in urls:
    comment_parsing(url)
#comment_parsing('http://api-t.iqiyi.com/qx_api/comment/get_video_comments?aid=15394177&albumid=0&categoryid=2&cb=fnsucc&escape=true&is_video_page=true&need_reply=true&need_subject=true&need_total=1&page=583&page_size=10&page_size_reply=3&qitan_comment_type=1&qitancallback=fnsucc&qitanid=15394177&qypid=01010011010000000000&reply_sort=hot&sort=hot&t=0.7062909778193278&tvid=0')