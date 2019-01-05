'''
Created on Jan 5, 2019

@author: Yusuke
'''
from animes.models import SubTitle

def UpdateOrCreate(tid, dic):
    
    for key in dic:
        SubTitle.objects.update_or_create(
            tid = tid,
            rno='{:02}'.format(int(key)),
            subtitle=dic[key].replace("/", "／").replace(":","：")
        )