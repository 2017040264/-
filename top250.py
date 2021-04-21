

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，文字匹配
import urllib.request, urllib.error  # 制定URL,获取网页数据
import xlwt  # 进行excel操作
import sqlite3   # 进行SQLite数据库操作

def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    datalist=getData(baseurl)
    print(len(datalist))

    # 3.保存数据
    savepath='豆瓣电影Top250.xls'
    savedata(savepath,datalist)

    dbpath = 'movie.db'
    savedata2DB(dbpath,datalist)

# 影片详情连接规则
findLink=re.compile(r'<a href="(.*?)">') # 创建正则表达式对象，表示字符串的模式
# 影片图片的链接
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)  # re.S忽略换行符
# 片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
# 评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
# 影片的相关内容
findBg=re.compile(r'<p class="">(.*?)</p>',re.S)

# 爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(10): #调用获取页面信息
        url=baseurl+str(i*25)
        html=askUrl(url) # 保存获取到的网页源码

        # 2.逐一解析数据
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.findAll('div',class_="item"): #查找符合要求的字符串
            #print(item)  # 测试，查看电影item
            data=[] # 保存一部电影的所有信息
            item=str(item)
            # 获取影片详情连接
            link=re.findall(findLink,item)[0]  # re库通过正则表达式查找指定的字符串
            data.append(link)

            imgScr=re.findall(findImgSrc,item)[0]
            data.append(imgScr)  #添加图片

            title=re.findall(findTitle,item)
            if len(title)==2:
                ctitle=title[0]
                data.append(ctitle) # 添加中文名

                otitle=title[1].replace('/','')
                data.append(otitle)  # 添加外国名
            else:
                data.append(title[0])
                data.append(' ') # 留空

            rating=re.findall(findRating,item)[0]
            data.append(rating) # 添加评分

            judge=re.findall(findJudge,item)[0]
            data.append(judge) # 评价人数

            inq=re.findall(findInq,item) # 添加概述
            if len(inq)!=0:
                inq=inq[0].replace('。','') #去掉句号
                data.append(inq)
            else:
                data.append(' ')

            bd=re.findall(findBg,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?',' ',bd) #去掉<br>
            bd=re.sub('/',' ',bd)
            data.append(bd.strip()) # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影信息放到datalist中
            #print(datalist)
            #break
        #break

    return  datalist


# 得到一个指定url的网页内容
def askUrl(url):
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36'
          } # 用户代理，伪装成浏览器
    req=urllib.request.Request(url,headers=head)
    html=''
    try:
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html



def savedata(savepath,datalist):
    wookbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    worksheet = wookbook.add_sheet('豆瓣电影top250')  # 创建工作表

    col=("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(8):
        worksheet.write(0,i,col[i])

    for i in range(250):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(8):
            worksheet.write(i+1, j, data[j])
    wookbook.save(savepath)  # 保存数据表

def savedata2DB(dbpath,datalist):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index]='"'+data[index]+'"'
        sql='''
        insert into movie250(
        info_link,img_link,cname,oname,score,rated,introduction,info)
        values(%s)
        '''%",".join(data)

        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql='''
    create table movie250
    (id integer primary key autoincrement,
    info_link text,
    img_link text,
    cname varchar,
    oname varchar,
    score numeric,
    rated numeric,
    introduction text,
    info text)
    '''
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



if __name__=='__main__':
    main()
    print('over!')