# -*- coding = utf-8 -*-
# @Time : 2021/4/21 15:20
# @Author : 陈凡亮
# @File : xlwt_test.py
# @Software : PyCharm
import  xlwt

wookbook=xlwt.Workbook(encoding='utf-8') # 创建workbook对象
worksheet=wookbook.add_sheet('sheet1') # 创建工作表
for i in range(1,10):
    for j in range(1,10):
        if i<=j:
            s=str(j)+'*'+str(i)+'='+str(i*j)
            worksheet.write(j-1,i-1,s) #写入数据，第一个参数：行,第二个参数：列，第三个参数：内容

wookbook.save('cfl.xls') #保存数据表