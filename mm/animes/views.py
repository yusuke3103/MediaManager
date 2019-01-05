import glob
import os.path
import re

from django.shortcuts import render, redirect
from django.template.context_processors import request

from animes.form import TitleListForm, SyoboCalTitleSearchForm, TitleResultForm
from animes.models import Title, SubTitle
from process import SyoboCalProcess, FileProcess
from animes.business import TitleBusiness, SubTitleBusiness

# Create your views here.
def index(request):
    
    list = TitleListForm
    lists = Title.objects.all().order_by('firstYear','firstMonth','firstEndYear','firstEndMonth')
    
    return render(request, 'animes/index.html', {'lists': lists})


def openRegist(request):
    search = SyoboCalTitleSearchForm
    return render(request, 'animes/regist.html', {'SearchForm':search})


def execSearch(request):
    search = SyoboCalTitleSearchForm(request.POST)
    result = SyoboCalProcess.TitleSearch(search.data['keyword'])
    return render(request, 'animes/regist.html', {'SearchForm':search, 'items':result})


def execRegist(request):    
    
    regist = TitleResultForm(request.POST)
    
    titledata = SyoboCalProcess.GetTitleFull(regist.data['pulldown'])

    for tid in titledata:
        
        TitleBusiness.UpdateOrCreate(tid,titledata)
    
        subtitledata = SyoboCalProcess.GetSubTitles(tid)
    
        SubTitleBusiness.UpdateOrCreate(tid,subtitledata)
    
        FileProcess.CreateDirectory(tid)
        
    return redirect('animes:index')


def openDetail(request):
    
    pTid = request.GET['tid']
    
    list = SubTitle.objects.filter(tid=pTid)
    
    return render(request, 'animes/detail.html', {'list' : list, 'tid': pTid})


def UpdateTitle(request):
    
    tid = request.GET['tid']
    
    subtitledata = SyoboCalProcess.GetSubTitles(tid)
    
    SubTitleBusiness.UpdateOrCreate(tid,subtitledata)

    list = SubTitle.objects.all().filter(tid=tid)
    return render(request, 'animes/detail.html', {'list' : list, 'tid': request.GET['tid']})   

def NameEditIndex(request):
    pTid = request.GET['tid']
    list = SubTitle.objects.filter(tid=pTid)
    os.chdir(Title.objects.get(tid=pTid).dirPath)
    files = glob.glob('*.*')
    
    lists = []
    for l in list:
        
        result = {}
        result['rno'] = l.rno
        result['subtitle'] = l.subtitle
        
        filename = "第" + l.rno + "話「" + l.subtitle + "」"
        
        isMatch = False
        for file in files:
            chk = filename + "." + os.path.splitext(file)[1][1:]
            
            if  chk == file :
                isMatch = True
                files.remove(file)
                
                break
        if isMatch == False:
            lists.append(result)

    return render(request, 'animes/nameedit.html', {'list' : lists, 'files':files, 'tid':pTid})   


def ExecChangeName(request):
    
    pTid = request.POST['tid']
    baseDir = Title.objects.get(tid=pTid).dirPath + "/"
    
    
    for key in request.POST:
        if "target" in key:
            pRno = key.replace("target-", '')
            befName = os.path.basename(request.POST['file-' + pRno])
            obj = SubTitle.objects.get(tid=pTid, rno=pRno)
            ext = os.path.splitext(request.POST['file-' + pRno])[1][1:]
            aftName = "第" + obj.rno + "話「" + obj.subtitle + "」." + ext
            os.rename(baseDir + befName, baseDir + aftName)
            print("変更前：" + baseDir + befName)
            print("変更後：" + baseDir + aftName)
    return redirect('animes:index')

def Repair(request):
    
    titles = Title.objects.all()
    
    for title in titles:
        
        subtitledata = SyoboCalProcess.GetSubTitles(title.tid)
    
        SubTitleBusiness.UpdateOrCreate(title.tid,subtitledata)
    
    return redirect('animes:index')