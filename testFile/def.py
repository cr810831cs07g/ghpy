
# -*- coding: utf8 -*-
import requests, re
from bs4 import BeautifulSoup
import  sensitive#, name, address, phone, id, mail, birthday

headers = {
    "User-Agent": 
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

params = {
    "q" : "asdadad" # query
#   "gl": "us"      # country
#   "hl": "en"      # language
}

result = requests.get("https://www.google.com/search?q=site%3Agcis.nat.gov.tw+ext%3Adoc+地址+台北市西華街1234號", 
                      headers=headers) #,
                      #params=params)
sp = BeautifulSoup(result.text, 'html.parser')
print(sp)
number_of_results = sp.select_one('#result-stats nobr').previous_sibling
print(number_of_results)

stories = sp.find_all(class_ = 'yuRUbf')
for link in stories:
    print(link.select_one("h3").getText())
    href = (link.find(class_ = "fl")).get('href')
    sensitive.sen(href)
    '''
    name.name(href)
    address.addr(href)
    id.id(href)
    birthday.bd(href)
    phone.ph(href)  
    mail.ma(href)
    if not href == None:
        print(href)
    '''