# -*- coding: utf8 -*-
import requests, re
from bs4 import BeautifulSoup
import sensitive, csv, pandas
import time, random


headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
           "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]


url = "https://webcache.googleusercontent.com/search?q=cache:_IzW3rfLW0QJ:https://www.tfai.org.tw/Content/TFI/PublicInfo/%25E4%25B8%25AD%25E8%258F%25AF%25E6%25B0%2591%25E5%259C%258B%25E9%259B%25BB%25E5%25BD%25B1%25E5%25B9%25B4%25E9%2591%2591%25E6%25B0%2591%25E5%259C%258B63%25E5%25B9%25B4.pdf+&cd=31&hl=zh-TW&ct=clnk&gl=tw"
res = sensitive.sen(url)
count = '疑似洩漏{}姓名,{}身分證,{}電話,{}信箱,{}地址,{}生日'.format(len(res["username"]),len(res["id"]),len(res["ph_no"]),len(res["em"]),len(res["address"]),len(res["bir"]))
remark = '姓名：{}\n身分證：{}\n電話：{}\n信箱：{}\n地址：{}\n生日：{}'.format(res["username"], res["id"], res["ph_no"], res["em"], res["address"], res["bir"])
print(remark)                    
                    #writer.writerow([link_count, links, count, url, remark])
  