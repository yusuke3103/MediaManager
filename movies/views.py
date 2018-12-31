from django.shortcuts import render

from movies.forms import SyoboCalTitleSearchForm, TitleRegistForm
from movies.process.SyoboCalProcess import SyoboCalProcess
from nltk.sem.chat80 import sea


# Create your views here.
def index(request):
	return render(request, 'movies/index.html')

def regist(request):
	
	if request.method == 'GET':
		search = SyoboCalTitleSearchForm
		return render(request, 'movies/regist.html',{'SearchForm' : search})
	elif request.method == 'POST':
		search = SyoboCalTitleSearchForm(request.POST)
		regist = TitleRegistForm
		regist.base_fields['pulldown'].choices = SyoboCalProcess.TitleSearch(search.data['keyword'])
		return render(request, 'movies/regist.html',{'SearchForm' : search, 'RegistForm' : regist})
		