# -*- coding = utf-8 -*-
# @Time : 2021/4/21 14:04
# @Author : 陈凡亮
# @File : re_test.py
# @Software : PyCharm
import re

# 创建模式对象
pat=re.compile('AA')
m=pat.search("CBA")
print(m)

m1=pat.search('CDSAA')
print(m1)

m2=pat.search("CGHFAAAAAAJH")
print(m2)

# 不创建模式对象
m3=re.search('asd',"GHGasd") #前面的是规则，后面是要被校验的
print(m3)


m4=re.findall('a',"jsjsakdsjajsja") # 前面是规则，后面是被校验的
print(m4)

m5=re.findall('[A-Z]+',"jsjGHKLsaJJkdsjajsja") # 前面是规则，后面是被校验的
print(m5)

#sub 分割、替换

# 建议在正则表达式中，被比较的字符串前加上'r',不用担心转义字符
m6=re.sub('a',"A","HGHahjha") # 用A替换a
print(m6)

a=r"\acbd\'"
b="\acbd\'"
print(a,b)