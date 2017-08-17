'''
 网址：https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1（see_lz表示只看楼主，1表示True,pn表示页码）
 时间：2017-08-11
 目标：百度贴吧爬虫
'''
import requests,re
from bs4 import BeautifulSoup

baseURL = 'https://tieba.baidu.com/p/3138733512'
seeLZ = '?see_lz=1'
def getPage(pageNum):
    url = baseURL + seeLZ + '&pn='+str(pageNum)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('h3.core_title_txt')[0].text
    page = soup.select('ul > li > span.red')[-1].text
    contents = soup.select('div.p_content > cc > div')
    with open('纯原创我心中的NBA2014-2015赛季现役50大.txt','a+') as file:
        for content in contents:
            floorLine = '\n****************************************************************\n'
            file.write(floorLine)
            file.write(content.text)

for i in range(1,6):
    getPage(i)