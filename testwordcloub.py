# -*- coding = utf-8 -*-
# @Time : 2021/4/29 15:36
# @Author : 陈凡亮
# @File : testwordcloub.py
# @Software : PyCharm

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

def main():
    con=sqlite3.connect('movie.db')
    cur=con.cursor()

    sql='select introduction from movie250'
    data=cur.execute(sql)
    text=''
    for item in data:
        text+=item[0]

    cut =jieba.cut(text)
    string =' '.join(cut)
    print(len(string))
    #print(string)

    img=Image.open(r'.\static\assets\img\camel.jfif')
    img_array=np.array(img) # 将图片转换为数组

    wc=WordCloud(background_color='black',
                 mask=img_array,
                 font_path='msyh.ttc')
    wc.generate_from_text(string)

    # 绘制图片
    fig=plt.figure(1)
    plt.imshow(wc)
    plt.axis('off') # 是否显示坐标轴

    #plt.show()
    plt.savefig(r'.\static\assets\img\word.png',dpi=500)

if __name__=='__main__':
    main()