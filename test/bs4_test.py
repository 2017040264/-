# -*- codeing = utf-8 -*-
# @Time : 2021/4/21 10:48
# @Author : 陈凡亮
# @File : bs4_test.py
# @Software : PyCharm
import re

from bs4 import BeautifulSoup

def main():
    file=open('baidu.html', 'rb')
    html=file.read().decode('utf-8')
    bs=BeautifulSoup(html,'html.parser')
    print(type(bs.title))
    print(bs.title)
    print(type(bs.title.string))
    print(bs.title.string)

    # 1.tag 标签及其内容，拿到它找到的第一个内容
    # 2.NavigableString 标签里面的内容
    # 3.BeautifulSoup 整个文档
    # 4.Comment 一种特殊的NavigableString，输出的不包括注释内容
    print(type(bs))
    print(bs.name)


    print(bs.a)
    print(bs.a.attrs)



    ##==================

    #文档的遍历
    print(bs.head.contents[1])
    #文档的搜索
    # 1.findall
    # 1.1字符串过滤 查找与字符串完全匹配的内容
    t_list=bs.findAll('a')
    print(t_list)
    # 1.2正则表达式搜索：使用search()方法来匹配内容
    t1_list=bs.findAll(re.compile('a'))
    print(t1_list)
    # 1.3方法：传入一个函数，根据函数要求来搜索
    def name_is_exits(tag):
        return tag.has_attr('name')
    t2_list=bs.findAll(name_is_exits)
    print(t2_list)

    # 2.kwargs
    k1=bs.findAll(id='head')
    print("*********************8")
    for item in k1:
        print(item)

    k2 = bs.findAll(class_=True)
    print("*********************8")
    for item in k2:
        print(item)

    # 3 text参数
    print("##########")
    t1=bs.findAll(text=['hao123','地图','贴吧'])
    for item in t1:
        print(item)

    print("##########")
    t2 = bs.findAll(text=re.compile('\d'))
    for item in t2:
        print(item)

    # 4 limit参数
    print("##########")
    l=bs.findAll('a',limit=3)
    for item in l:
        print(item)


    # CSS选择器
    print(bs.select('title')) #通过标签查找
    print(bs.select('.mnav')) #通过类名查找
    print("XXXXXXXXX")
    print(bs.select('#u1')) # 通过id查找
    print(bs.select('a[class="bri"]')) #通过属性查找
    print(bs.select('head > a')) #通过子标签查找3



if __name__=='__main__':
    main()