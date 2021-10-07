# -*- coding: utf8 -*-
import requests, re

def bd(url):
    vids_pattern = r'((?:19\d{2}|20[01]\d|202[0-2])(?:年|/|-|)(?:0[1-9]|1[0-2]|[1-9])(?:月|/|-|)(?:0\d|3[0-1]|[1-9]|[1-2]\d))'
    roc_pattern = r'((?:^0[2-9]\d|10\d|110|^[2-9][\d])(?:年|/|-|)(?:0\d|1[0-2]|[1-9])(?:月|/|-|)(?:0\d|3[0-1]|[1-9]|[1-2]\d)$)'
    birth = requests.get(url).text
    vids_day = re.findall(vids_pattern, birth)
    roc_day = re.findall(roc_pattern, birth)
    i = 0
    for vid_bir in vids_day:
        i += 1
        print("{} :西元{}".format(i,vid_bir))

    for roc_bir in roc_day:
        i += 1
        print("{} :民國{}".format(i,roc_bir))
        #print("{} :{}".format(i, hm))