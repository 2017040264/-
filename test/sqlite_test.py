# -*- coding = utf-8 -*-
# @Time : 2021/4/21 16:31
# @Author : 陈凡亮
# @File : sqlite_test.py
# @Software : PyCharm

import sqlite3

def connect():
    conn=sqlite3.connect('test.db') #打开或者创建数据库
    print('Open database sucessfully!')
    return conn

def creat_tabel(conn):
    c=conn.cursor() #获取游标
    sql='''
        create table company
        (id int primary key not null,
        name text not null,
        age int not null);
        
        '''
    c.execute(sql) # 执行sql
    conn.commit() # 提交数据库操作
    conn.close() # 关闭数据库操作

def insert(conn):
    c = conn.cursor()  # 获取游标
    sql2='''
        insert into company(id,name,age)
        values(1,'haha',20);
    '''
    c.execute(sql2) # 执行sql
    conn.commit() # 提交数据库操作
    conn.close() # 关闭数据库操作
    print('插入成功')

def find(coon):
    c = coon.cursor()  # 获取游标
    sql2 = '''
            select c.id,c.age,c.name from company c;
        '''
    cursor=c.execute(sql2)  # 执行sql
    for row in cursor:
        print(row)
    coon.close()  # 关闭数据库操作


if __name__=="__main__":
    coon=connect()
    #creat_tabel(coon)
    #insert(coon)
    find(coon)

# 查询数据