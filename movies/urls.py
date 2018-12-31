from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
	path('', views.index, name='index'),
	path('/regist', views.regist, name='RegistIndex'),
	path('/regist/search', views.regist, name='RegistSearch'),
]