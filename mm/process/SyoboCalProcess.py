'''
Created on Dec 30, 2018

@author: Yusuke
'''
import json
import re
import urllib

from bs4 import BeautifulSoup


def TitleSearch(keyword):
    BASE_URL = 'http://cal.syoboi.jp/find?sd=0&kw=keyword&ch=&st=&cm=&r=0&rd=&v=0'
    url = BASE_URL.replace('keyword', urllib.parse.quote(keyword))
    
    print(url)
    
    res = urllib.request.urlopen(url)
    
    soup = BeautifulSoup(res, "html.parser")
    
    list = []
    
    for a in soup.find_all(href=re.compile("tid")):
        map = {'tid':a.get('href').replace("/tid/", ""),'title':a.string}
        list.append(map)

    return list

def GetTitleFull(tid):
    BASE_URL = 'http://cal.syoboi.jp/json.php?Req=TitleFull&TID=keyword'
    url = BASE_URL.replace("keyword", tid)
    res = urllib.request.urlopen(url)
    
    json_dict = json.loads(res.read())
    
    json_dict['Titles']
        
    return json_dict['Titles']

def GetSubTitles(tid):
    BASE_URL = 'http://cal.syoboi.jp/json.php?Req=SubTitles&TID=keyword'
    url = BASE_URL.replace("keyword", tid)
    res = urllib.request.urlopen(url)
    
    json_dict = json.loads(res.read())
    
    return json_dict['SubTitles'][tid]
