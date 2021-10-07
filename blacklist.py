
   
# -*- coding: utf8 -*-
def filterList(list):
    result = []
    with open('blacklist.txt', 'r', encoding='UTF-8') as in_fh:
        blacklist = in_fh.read().splitlines()
        for text in list:
            #utf8Text = text.encode('UTF-8')
            AllowEntry = True
            for badEntry in blacklist:
                #utf8BadEntry = badEntry.encode('UTF-8')                
                #if utf8Text == utf8BadEntry:
                if badEntry in text:
                    AllowEntry = False
                    break                        
            if AllowEntry:
                result.append(text)                
    return result