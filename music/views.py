from django.http import HttpResponse
#from django.shortcuts import render

# view is simple function/class that returns html
def index(request):
    return HttpResponse("<h1>This is the music app homepage</h1>")

def detail(request,id):
    return HttpResponse("<h1>Detail for music with id=" + str(id) + "</h1>")
