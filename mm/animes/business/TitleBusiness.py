'''
Created on Jan 5, 2019

@author: Yusuke
'''
from animes.models import Title
from process import SyoboCalProcess


def UpdateOrCreate(tid, dic):
    
    Title.objects.update_or_create(
        tid=tid,
        title=dic[tid]['Title'].replace("/", "／").replace(":","："),
        firstYear=dic[tid]['FirstYear'],
        firstMonth=dic[tid]['FirstMonth'],
        firstEndYear=dic[tid]['FirstEndYear'],
        firstEndMonth=dic[tid]['FirstEndMonth'],
        comment=dic[tid]['Comment'],
        dirPath='/Volumes/HDD2/Videos/' + dic[tid]['Title'].replace("/", "／").replace(":","："),
    )
