# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:38:38 2017

@author: Kismet
"""


import requests
import json
import pymongo


client = pymongo.MongoClient('localhost',27017)
kismet = client['kismet']
half_life = kismet['half_life']

def send_request(text):
    # 基本API server
    # POST http://101.37.25.146/beta/emotion

    try:
        response = requests.post(
            url="****************",
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": "********",
            },
            data=json.dumps({
                "sentence": text,
                "emotionModel": 2
            })
        )
        # print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        json1_data = json.loads(response.content.decode("utf-8"))
        print (json1_data)
        #half_life.insert_one(json1_data)
    except requests.exceptions.RequestException:
        return('HTTP Request failed')


with open(path,'r',encoding='utf-8') as file:
    for line in file.readlines():
        data = line.split('\t')[0]
        send_request(data)
