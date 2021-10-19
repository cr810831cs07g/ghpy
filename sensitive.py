# -*- coding: utf8 -*-
import requests, re
from bs4 import BeautifulSoup
import blacklist
import os


#	text = re.sub('<.*?>', '', html, flags=re.S)   顯示前端字串

#df = { 'TITLE':[], 'URL':[], 'RESULT':[] }   10/18

def sen(url):          
    # --------------比對姓名-------------------------
    os.chdir('/Users/naco/Desktop/regex_name') # 黑名單字串路徑

    html = requests.get(url).text
    #soup = BeautifulSoup(html.text, 'html.parser')
    soup = re.sub(r'(?s)<meta.*?</head>', '', html)    # 濾掉google提示
    soup = re.sub('<.*?>', '', soup, flags=re.S)
    
    #s = soup.text.encode()  #字串符轉譯
    #temp = s.decode('utf-8')  
    
    pattern="[\u9673|\u6797|\u9ec3|\u5f35|\u674e|\u738b|\u5433|\u5289|\u8521|\u694a\u8a31|\u912d|\u8b1d|\u6d2a|\u90ed|\u90b1|\u66fe|\u5ed6|\u8cf4|\u5f90\u5468|\u8449|\u8607|\u838a|\u5442|\u6c5f|\u4f55|\u856d|\u7f85|\u9ad8\u6f58|\u7c21|\u6731|\u937e|\u6e38|\u5f6d|\u8a79|\u80e1|\u65bd|\u6c88\u4f59|\u76e7|\u6881|\u8d99|\u984f|\u67ef|\u7fc1|\u9b4f|\u5b6b|\u6234\u8303|\u65b9|\u5b8b|\u9127|\u675c|\u5085|\u4faf|\u66f9|\u859b|\u4e01\u5353|\u962e|\u99ac|\u8463|\u6e29|\u5510|\u85cd|\u77f3|\u8523|\u53e4\u7d00|\u59da|\u9023|\u99ae|\u6b50|\u7a0b|\u6e6f|\u9ec4|\u7530|\u5eb7\u59dc|\u767d|\u6c6a|\u9112|\u5c24|\u5deb|\u9418|\u9ece|\u6d82|\u9f94\u56b4|\u97d3|\u8881|\u91d1|\u7ae5|\u9678|\u590f|\u67f3|\u51c3|\u90b5\u9322|\u4f0d|\u502a|\u6eab|\u4e8e|\u8b5a|\u99f1|\u718a|\u4efb|\u7518\u79e6|\u9867|\u6bdb|\u7ae0|\u53f2|\u5b98|\u842c|\u4fde|\u96f7|\u7c98\u9952|\u95d5|\u51cc|\u5d14|\u5c39|\u5b54|\u8f9b|\u6b66\u8f9c|\u9676|\u6613|\u6bb5|\u9f8d|\u97cb|\u845b|\u6c60|\u5b5f|\u891a\u6bb7|\u9ea5|\u8cc0|\u8cc8|\u83ab|\u6587|\u7ba1|\u95dc|\u5411|\u5305\u4e18|\u6885|\u83ef|\u5229|\u88f4|\u6a0a|\u623f|\u5168|\u4f58\u5de6|\u82b1|\u9b6f|\u5b89|\u9b91|\u90dd|\u7a46|\u5857|\u90a2|\u84b2\u6210|\u8c37|\u5e38|\u95bb|\u7df4|\u76db|\u9114|\u803f|\u8076|\u7b26\u7533|\u795d|\u7e46|\u967d|\u89e3|\u66f2|\u5cb3|\u9f4a|\u7c43|\u61c9\u55ae|\u8212|\u7562|\u55ac|\u9f8e|\u7fdf|\u725b|\u911e|\u7559|\u5b63\u8983|\u535c|\u9805|\u51c3|\u55bb|\u5546|\u6ed5|\u7126|\u8eca|\u8cb7\u865e|\u82d7|\u621a|\u725f|\u96f2|\u5df4|\u529b|\u827e|\u6a02|\u81e7\u53f8|\u6a13|\u8cbb|\u5c48|\u5b97|\u5e78|\u885b|\u5c1a|\u9773|\u7941\u8af6|\u6842|\u6c99|\u6b12|\u5bae|\u8def|\u5201|\u6642|\u9f90|\u77bf\u67f4|\u67cf|\u913a|\u8ac7|\u67e5|\u970d|\u968b|\u9594|\u9ad9|\u7ac7\u677e|\u5409|\u752f|\u9072|\u5132|\u98a8|\u91cb|\u4ef2|\u5189|\u9102\u6e5b|\u4ec7|\u6771|\u5321|\u69ae|\u4f0a|\u660c|\u5a41|\u862d|\u51b7\u535e|\u6851|\u664f|\u5c91|\u88d8|\u59ec|\u5e2d|\u8499|\u521d|\u5340][\u4e00-\u9fa5]{1,3}"#中文正規表示
    regex = re.compile(pattern) #生成正則對象 
    results =  regex.findall(soup)  #匹配
    filterList = blacklist.filterList(results)
    i = 0
    for result in filterList:
        i += 1
        print("{}".format(result))
    name_count = i
    #-----------------------------------------------

    #--------------比對身分證-------------------------
    
#def id(url):                
    id_reg = "[a-zA-z][12][0-9]{8}"

    
    result = re.findall(id_reg, soup)
    i = 0
    for results in result:
        i += 1
        print("{} :{}".format(i, results))
    id_count = i
    #-----------------------------------------------    
    
#def ph(list):               # 比對電話
    phone_reg = r'(?:0|886-?)9\d{2}(?:\d{6}|-\d{6}|-\d{3}-\d{3}?)'
    hm_reg = r'(\d{4}-\d{7}|\d{3}-\d{8}|0[24]-\d{8}|0[24]-\d{4}-\d{4}|0[3-8]-\d{7}|0[3-8]-\d{3}-\d{4}|(?:037|082|089)-\d{6}|(?:037|082|089)-\d{3}-\d{3}|049-\d{7}|049-\d{3}-\d{4}|0836-\d{5})'

    
    phones = re.findall(phone_reg, soup)
    hms = re.findall(hm_reg, soup)

    i = 0
    for phone in phones:
        i += 1
        print("{} :{}".format(i, phone))
    for hm in hms:
        i += 1
        #print("{} :{}".format(i, hm))
    phone_count = i
    #-----------------------------------------------
#def ma(url):                # 比對信箱

    regex = r"([a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    
    emails = re.findall(regex, soup)
    i = 0
    for email in emails:
        i += 1
        #print("{} :{}".format(i, email))
    mail_count = i
    #-----------------------------------------------
#def addr(list):             # 比對地址
    pattern= '[\u53f0\u5317\u5e02].{5,20}[\u865f]' 

    #s = soup.text.encode()  
    #temp = s.decode('utf-8') 
    
    regex = re.compile(pattern) 
    results =  regex.findall(soup) 
    i = 0
    for addr in results :
        i += 1
        #print ("{} :{}".format(i,addr))
    addr_count = i
    #-----------------------------------------------
#def bd(url):                # 比對生日
    vids_pattern = r'((?:^19\d{2}|20[01]\d|202[0-2])(?:年|/|-|)(?:0[1-9]|1[0-2]|[1-9])(?:月|/|-|)(?:0\d|3[0-1]|[1-9]|[1-2]\d))'
    roc_pattern = r'((?:^0[2-9]\d|10\d|110|^[2-9][\d])(?:年|/|-|)(?:0\d|1[0-2]|[1-9])(?:月|/|-|)(?:0\d|3[0-1]|[1-9]|[1-2]\d)$)'
    
    
    vids_day = re.findall(vids_pattern, soup)
    roc_day = re.findall(roc_pattern, soup)
    i = 0
    for vid_bir in vids_day:
        i += 1
        #print("{} :西元{}".format(i,vid_bir))

    for roc_bir in roc_day:
        i += 1
        #print("{} :民國{}".format(i,roc_bir))
    bd_count = i
    #-----------------------------------------------
    print("疑似洩漏{}姓名,{}身分證,{}電話,{}信箱,{}地址,{}生日".format(name_count, id_count, phone_count, mail_count, addr_count, bd_count))
    print('-----------------------------------------------')
