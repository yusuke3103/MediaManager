from django.shortcuts import render, redirect

from animes.form import SyoboCalTitleSearchForm, TitleResultForm, TitleListForm
from animes.models import Title
from process.SyoboCalProcess import SyoboCalProcess


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
        regist = TitleResultForm
        
        regist.base_fields['pulldown'].choices = []
        for obj in SyoboCalProcess.TitleSearch(search.data['keyword']):
            regist.base_fields['pulldown'].choices.append(obj)
#         regist.base_fields['pulldown'].choices = SyoboCalProcess.TitleSearch(search.data['keyword'])
        return render(request, 'animes/regist.html',{'SearchForm':search, 'RegistForm':regist})

def execRegist(request):    
    regist = TitleResultForm(request.POST)
    data = SyoboCalProcess.GetTitleFull(regist.data['pulldown'])
    

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
