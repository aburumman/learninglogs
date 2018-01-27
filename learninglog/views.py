from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Entry

def index(request):
    return HttpResponse("<p> This is the index page </p>")

def places(request):
    page_title = 'The Places'
    #context = {page_title: 'page_title'}
    return render(request, 'learninglog/places.html')


# Create your views here.
