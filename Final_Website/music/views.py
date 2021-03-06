from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Album
from .forms import RegisterForm, LoginForm
from django.db.models import Q
from django.utils import timezone


class SearchView(generic.ListView):
    template_name = 'music/search.html'
    context_object_name = 'all_songs'
    def get_queryset(self):
        queryset_list = Song.objects.all()
        print(self.request)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(song_title__icontains=query)
            )
        print(queryset_list)
        return queryset_list



class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user =  form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

class LoginView(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data
    def post(self, request):
        form = self.form_class(request.POST)
        print(form)

        if form.is_valid():

            # user =  form.save(commit=False)

            # print(user)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            print(user)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        else:
            print("Form invalid")

        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('music:index')



