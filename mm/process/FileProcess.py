'''
Created on Jan 5, 2019

@author: Yusuke
'''
import os

from animes.models import Title
from django.shortcuts import redirect


DEBUG = True


def FileRename():
    pass

def CreateDirectory(tid):
    
    path = Title.objects.get(tid=tid)
    
    if os.path.exists(path) == False:
        os.makedirs(path)
    