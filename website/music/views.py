from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
	print("INDEX")
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
	print("hello")
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request, 'music/detail.html', {'album': album})