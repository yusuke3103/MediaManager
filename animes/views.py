from django.shortcuts import render

from animes.form import SyoboCalTitleSearchForm, TitleRegistForm
from process.SyoboCalProcess import SyoboCalProcess
from anaconda_navigator.utils.py3compat import request


# Create your views here.
def index(request):
    return render(request, 'animes/index.html')

def openRegist(request):
    search = SyoboCalTitleSearchForm
    return render(request, 'animes/regist.html', {'SearchForm':search})


def execSearch(request):
        search = SyoboCalTitleSearchForm(request.POST)
        regist = TitleRegistForm
        regist.base_fields['pulldown'].choices = []
        regist.base_fields['pulldown'].choices = SyoboCalProcess.TitleSearch(search.data['keyword'])
        return render(request, 'animes/regist.html',{'SearchForm':search, 'RegistForm':regist})
    
def execRegist(request):
    return render(request, 'animes/index.html')