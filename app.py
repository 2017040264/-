# -*- coding = utf-8 -*-
# @Time : 2021/4/26 10:30
# @Author : 陈凡亮
# @File : app.py
# @Software : PyCharm

from flask import Flask,render_template,request
import sqlite3
import jieba

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/movie')
def movie():
    datalist=[]
    con=sqlite3.connect('movie.db')
    cur=con.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('movie.html',movies=datalist)


@app.route('/score')
def score():
    scores = [] # 评分
    count_scores=[] # 每个评分统计出的电影数量
    con = sqlite3.connect('movie.db')
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scores.append(str(item[0]))
        count_scores.append(item[1])
    cur.close()
    con.close()
    return render_template('score.html',scores=scores,count_scores=count_scores)


@app.route('/word')
def word():
    return render_template('word.html')


@app.route('/team')
def team():
    return render_template('team.html')


if __name__=='__main__':
    app.run(debug=True)
