from django.urls import path
from . import views

app_name = 'animes'
urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.openRegist, name='OpenRegist'),
    path('search', views.execSearch, name='ExecSearch'),
    path('regist', views.execRegist, name='ExecRegist'),
    path('detail', views.openDetail, name="OpenDetails"),
    path('updSub', views.UpdateTitle, name="GetSubTitles"),
    path('CreateDirectory', views.CreateDirectory, name="CreateDirectory"),
    path('NameEditIndex', views.NameEditIndex, name="NameEditIndex"),
    path('ExecChangeName', views.ExecChangeName, name="ExecChangeName")
]
