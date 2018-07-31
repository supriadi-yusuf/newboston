from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .models import Album, Song
from .forms import UserForm

class IndexView(generic.ListView): # there is no rule for class name here
    template_name = 'music/album_list.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()
    #model = Album

class DetailView(generic.DetailView): # there is no rule for class name here
    model = Album
    template_name = 'music/album_detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music_app:album-list')

class UserFormView(View):
    form_class = UserForm
    template_name = "music/registration.html"

    # display blank form
    def get( self, request):
        form = self.form_class(None) # None means that there is no information is passed
        return render( request, self.template_name, { 'form': form})

    # process form data
    def post( self, request):
        form = self.form_class( request.POST) # request.POST means passing form data
        if form.is_valid():
            user = form.save(commit=False) # create object but do not enter data to db ( not save to db)

            # clean / normalize data. clean means data is formatted properly.
            username = form.cleaned_data['username'] # data is returned in plain text
            password = form.cleaned_data['password'] # data is returned in plain text
            # to change / save user.password we can user user.set_password(password) instead of user.password = password
            # because password should be stored in encrypted format
            user.set_password(password)
            user.save() # finally save user into db

            # return user object if credential is correct
            user = authenticate( username=username, password=password)
            if user is not None:
                if user.is_active:
                    login( request, user) # logging the user in
                    # after the user is logging in, so we can retrieve user data
                    # example : request.user.username, request.user.is_active, etc.
                    return redirect('music_app:album-list') # directing to url named 'music_app:album-list'

            return render( request, self.template_name, { 'form': form})

class LogoutView(View):
    def get( self, request):
        #user = request.user
        #if user is not None:
        logout( request)
        return redirect('music_app:album-list')
