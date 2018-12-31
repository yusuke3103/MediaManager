'''
Created on 2018/12/30

@author: Yusuke
'''
from _ast import keyword

from django import forms
from movies.process.SyoboCalProcess import SyoboCalProcess

TEMP = [(1,"テスト")]

class SyoboCalTitleSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)

class TitleRegistForm(forms.Form):
    
    pulldown = forms.ChoiceField(widget=forms.Select, choices=TEMP)