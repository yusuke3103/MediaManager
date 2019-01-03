import glob
import os.path
import re

from django.shortcuts import render, redirect
from django.template.context_processors import request
from pip._internal import req

from animes.form import TitleListForm, SyoboCalTitleSearchForm, TitleResultForm
from animes.models import Title, SubTitle
from process.SyoboCalProcess import SyoboCalProcess


DEBUG = True


# Create your views here.
def index(request):
    
    list = TitleListForm
    lists = Title.objects.all()
    
    return render(request, 'animes/index.html', {'lists': lists})


def openRegist(request):
    search = SyoboCalTitleSearchForm
    return render(request, 'animes/regist.html', {'SearchForm':search})


def execSearch(request):
        search = SyoboCalTitleSearchForm(request.POST)
#         regist = TitleResultForm
#         
#         regist.base_fields['pulldown'].choices = []
#         for obj in SyoboCalProcess().TitleSearch(search.data['keyword']):
#             regist.base_fields['pulldown'].choices.append(obj)
#         regist.base_fields['pulldown'].choices = SyoboCalProcess.TitleSearch(search.data['keyword'])
#         return render(request, 'animes/regist.html', {'SearchForm':search, 'RegistForm':regist})

        result = SyoboCalProcess().TitleSearch(search.data['keyword'])
        return render(request, 'animes/regist.html', {'SearchForm':search, 'items':result})


def execRegist(request):    
    regist = TitleResultForm(request.POST)
    data = SyoboCalProcess().GetTitleFull(regist.data['pulldown'])

    Title(
        tid=data['TID'],
        title=data['Title'],
        firstYear=data['FirstYear'],
        firstMonth=data['FirstMonth'],
        firstEndYear=data['FirstEndYear'],
        firstEndMonth=data['FirstEndMonth'],
        comment=data['Comment'],
    ).save()
    
    return redirect('animes:index')


def openDetail(request):
    
    pTid = request.GET['tid']
    
    list = SubTitle.objects.filter(tid=pTid)
    
    return render(request, 'animes/detail.html', {'list' : list, 'tid': pTid})


def UpdateTitle(request):
      
    dic = SyoboCalProcess().GetSubTitles(tid=request.GET['tid'])
      
    for key in dic:
          
        SubTitle.objects.update_or_create(
            tid=request.GET['tid'],
            rno='{:02}'.format(int(key)),
            subtitle=dic[key]
        )

    list = SubTitle.objects.all().filter(tid=request.GET['tid'])
    return render(request, 'animes/detail.html', {'list' : list, 'tid': request.GET['tid']})   


def CreateDirectory(request):
    
    pTid = request.GET['tid']
    
    obj = Title.objects.get(tid=pTid)
    
    path = GetDir(pTid)
    
    print(path)
    
    if os.path.exists(path) == False:
        os.makedirs(path)
    
    return redirect('animes:index')


def NameEditIndex(request):
    pTid = request.GET['tid']
    list = SubTitle.objects.filter(tid=pTid)
    path = GetDir(pTid)
    files = glob.glob(path + '/*')
    return render(request, 'animes/nameedit.html', {'list' : list, 'files':files, 'tid':pTid})   


def ExecChangeName(request):
    
    pTid = request.POST['tid']
    
    for key in request.POST:
        if "target" in key:
            pRno = key.replace("target-", '')
            baseDir = os.path.dirname(request.POST['file-' + pRno]) + "/"
            befName = os.path.basename(request.POST['file-' + pRno])
            obj = SubTitle.objects.get(tid=pTid, rno=pRno)
            ext = os.path.splitext(request.POST['file-' + pRno])[1][1:]
            aftName = "第" + obj.rno + "話「" + obj.subtitle + "」." + ext
            os.rename(baseDir + befName, baseDir + aftName)
            print("変更前：" + baseDir + befName)
            print("変更後：" + baseDir + aftName)
    return redirect('animes:index')

      
def GetDir(pTid):
    
    obj = Title.objects.get(tid=pTid)
    
    if DEBUG == True:
        return obj.dirPath.replace('/Volumes/HDD2/Videos', '/Users/Yusuke/workspace/test')
    else:
        return obj.dirPath
