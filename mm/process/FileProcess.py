'''
Created on Jan 5, 2019

@author: Yusuke
'''
import copy
import glob
import os

from django.shortcuts import redirect

from animes.models import Title, SubTitle


DEBUG = True


def FileRename(tid, subtitle, rno, path):
    
    name, ext = os.path.splitext(path)
    dir = os.path.dirname(path)
    
    bef = dir + "/" + '第{rno}話「{subtitle}」{ext}'.format(rno=rno, subtitle=subtitle, ext=ext)
    
    os.rename(path, bef)
    
    return bef


def CreateDirectory(tid):
    
    title = Title.objects.get(tid=tid)
    
    if os.path.exists(title.dirPath) == False:
        os.makedirs(title.dirPath)


def GetFiles(tid):
    
    datas = SubTitle.objects.filter(tid=tid)
    
    path = Title.objects.get(tid=tid).dirPath
    files = glob.glob(path + "/*")
    
    loop = copy.copy(files)
    
    for file in loop:
        
        f = datas.filter(path=file)

        if len(f) > 0:
            files.remove(file)
    
    return files

