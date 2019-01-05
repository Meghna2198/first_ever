from django.conf.urls import url
from .import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),


    #music/search/
    url(r'^search/$', views.SearchView.as_view(), name = 'search'),

    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),

    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'^album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]
