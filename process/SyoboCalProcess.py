'''
Created on Dec 30, 2018

@author: Yusuke
'''
import json
import re
import urllib

from bs4 import BeautifulSoup


class SyoboCalProcess:
    
    def TitleSearch(self):
        BASE_URL = 'http://cal.syoboi.jp/find?sd=0&kw=keyword&ch=&st=&cm=&r=0&rd=&v=0'
        url = BASE_URL.replace('keyword', urllib.parse.quote(self))
        
        print(url)
        
        res = urllib.request.urlopen(url)
        
        soup = BeautifulSoup(res,"html.parser")
        
        list = []
        
        for a in soup.find_all(href=re.compile("tid")):
            
            t = (a.get('href').replace("/tid/",""), a.string)
            
            list.append(t)
    
        print (list)
    
        return list

    def GetTitleFull(self):
        BASE_URL = 'http://cal.syoboi.jp/json.php?Req=TitleFull&TID=keyword'
        url = BASE_URL.replace("keyword", self)
        res = urllib.request.urlopen(url)
        
        json_dict = json.loads(res.read())
        
        
        result = {}
        for key in json_dict['Titles'][self]:
            result[key] = json_dict['Titles'][self][key]
            
        return result