'''
Created on Dec 30, 2018

@author: Yusuke
'''
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
