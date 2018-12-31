'''
Created on 2018/12/30

@author: Yusuke
'''
from django import forms

class SyoboCalTitleSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)

    