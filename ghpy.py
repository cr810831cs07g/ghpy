# -*- coding: utf8 -*-
import requests, re
from bs4 import BeautifulSoup
import sensitive, csv

headers = {
    "User-Agent": 
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

params = {
    "q" : "asdadad" # query
#   "gl": "us"      # country
#   "hl": "en"      # language
}
# Google hacking語法
site = input("")
keyword = """+("證號"+|+"姓名"+|+"生日"+|+"出生"+|+"電話"+|+"手機"+|+"護照"+|+"婚姻"+|+"家庭"+|+"教育"+|+"職業"+|+"病歷"+|+"聯絡")"""
ext = "+ext:doc+|+ext:docx+|+ext:xls+|+ext:xlsx+|+ext:ppt+|+ext:pptx+|+ext:pdf+|+ext:csv+|+ext:odt+|+ext:rtf+|+ext:sxw+|+ext:csv+|+ext:pps"

result = requests.get("https://www.google.com/search?q=site%3A"+site+keyword+ext, 
                      headers=headers) #,
                      #params=params)
with open(site + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['No', 'Title', 'Rusult', 'URL'])

    sp = BeautifulSoup(result.text, 'html.parser')

    number_of_results = sp.select_one('#result-stats nobr').previous_sibling    # 顯示搜尋結果總數
    print(number_of_results)
    page_no = 1
    print("-----{}PAGE-----".format(page_no))
    stories = sp.find_all(class_ = 'yuRUbf')
    link_count = 0
    for link in stories:
        link_count += 1
        links = link.select_one("h3").getText()
        print("{}:{}".format(link_count,links))
        href = link.find("a", {"class":"fl"})
        #print(href)
        try:
            url = href.get('href')
            print(url)
            res = sensitive.sen(url)
            count = '疑似洩漏{}姓名,{}身分證,{}電話,{}信箱,{}地址,{}生日'.format(len(res["username"]),len(res["id"]),len(res["ph_no"]),len(res["em"]),len(res["address"]),len(res["bir"]))
            writer.writerow([link_count, links, count, url])
        except:
            print("----Web cache no here!----")
            writer.writerow([link_count, links, 'NO web cache'])
    while True:
        try:
            page = sp.find(id="pnnext").get('href')
            page_no += 1
            print("-----{}PAGE-----".format(page_no))
            result = requests.get("https://www.google.com/" + page, 
                            headers=headers) #,
                            #params=params)
            sp = BeautifulSoup(result.text, 'html.parser')

            stories = sp.find_all(class_ = 'yuRUbf')

            for link in stories:
                link_count += 1
                print(link.select_one("h3").getText())
                href = link.find("a", {"class":"fl"})
                try:
                    url = href.get('href')
                    print(url)
                    res = sensitive.sen(url)
                    count = '疑似洩漏{}姓名,{}身分證,{}電話,{}信箱,{}地址,{}生日'.format(len(res["username"]),len(res["id"]),len(res["ph_no"]),len(res["em"]),len(res["address"]),len(res["bir"]))
                    writer.writerow([link_count, links, count, url])
                    
                except:
                    print("Web cache no here!")
                    writer.writerow([link_count, links, 'NO web cache'])
        except:
            pass
            break
        
    print("\\\\\\THIS'S END//////")
    
