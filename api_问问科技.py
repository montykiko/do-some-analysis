# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:38:38 2017

@author: Kismet
"""


import requests
import json

def send_request(text,type):
    try:
        response = requests.post(
            url="https://api.kismet-emotions.com/dev/negativealerttwoside",
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": "Basic d2VpcWl0ZXN0OndlaXFpQVBJ",
            },
            data=json.dumps({
                "sentence": text,
                "type": type
            })
        )
        json1_data = json.loads(response.content.decode("utf-8"))
        emotion = json1_data['emotion']
        threshold = json1_data['threshold']
        return emotion,threshold
    except requests.exceptions.RequestException:
        return('HTTP Request failed')


with open(r'C:/Users/Kismet/Documents/我的坚果云/语忆科技有限公司/问问科技分析/wenwen_clean_0814.txt','r',encoding = 'utf-8') as file:
    with open(r'C:/Users/Kismet/Documents/我的坚果云/语忆科技有限公司/问问科技分析/test.txt ','w',encoding='utf-8') as f:
        for line in file.readlines():
            content = line.split('\t')[3].strip('"')
            Type = line.split('\t')[-1]
            if Type == 2:
                sentence = line.strip() + '\t' + send_request(content,2)[0] + '\t' + str(send_request(content,2)[1]) + '\n'
            else:
                sentence = line.strip() + '\t' + send_request(content,1)[0] + '\t' + str(send_request(content,2)[1]) + '\n'
            f.write(sentence)
            print (sentence)
    f.close()
    file.close()


