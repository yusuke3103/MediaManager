from django.shortcuts import render


def index(request):
	render(request, 'movies/index.html')
