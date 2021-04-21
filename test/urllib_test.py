# -*- codeing = utf-8 -*-
# @Time : 2021/4/21 9:40
# @Author : 陈凡亮
# @File : urllib_test.py
# @Software : PyCharm

import urllib.request
import urllib.parse
import urllib.error
# 获取一个get请求
def get():
    url='http://www.baidu.com'
    response=urllib.request.urlopen(url)
    print(response.read().decode('utf-8'))# 对获取的网页源码进行utf-8解码

# 获取一个post请求
def post():
    data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
    url1='http://httpbin.org/post'
    res1=urllib.request.urlopen(url1,data=data)
    print(res1.status)
    print(res1.read().decode('utf-8'))

# 超时处理
def timeout():
    url1 = 'http://httpbin.org/get'
    try:
        res1 = urllib.request.urlopen(url1,timeout=0.01)
        print(res1.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print('tiem out!')

# 直接爬取豆瓣，被识别为爬虫，418
def douban():
    url='https://www.douban.com'
    response = urllib.request.urlopen(url)
    print(response.status)
    print(response.read().decode('utf-8'))  # 对获取的网页源码进行utf-8解码

# 爬取豆瓣，伪装成浏览器
def douban_updata():
    url = 'https://www.douban.com'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36'
    }
    req=urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(req)
    print(response.status)
    print(response.read().decode('utf-8'))


if __name__=='__main__':
    #get()
    #post()
    #timeout()
    #douban()
    douban_updata()