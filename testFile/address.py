# -*- coding: utf8 -*-
import requests, re
from bs4 import BeautifulSoup
def addr(list):
    sex = requests.get(list) #純屬學術研究使用
    soup = BeautifulSoup(sex.text, 'html.parser')

    s = soup.text.encode()  #此处必须进行字符串转义

    temp = s.decode('utf-8') 
    pattern= '[\u53f0\u5317\u5e02].{5,20}[\u865f]' #中文正则表达式

    regex = re.compile(pattern) #生成正则对象 


    results =  regex.findall(temp)  #匹配
    for result in results :  #迭代遍历出内容
        print (result)