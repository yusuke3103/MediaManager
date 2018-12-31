from django.shortcuts import render

from movies.forms import SyoboCalTitleSearchForm


# Create your views here.
def index(request):
	return render(request, 'movies/index.html')

def regist(request):
	search = SyoboCalTitleSearchForm
	return render(request, 'movies/regist.html',{'SearchForm' : search})
