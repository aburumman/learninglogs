from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Entry
from .forms import TopicForm

def index(request):
    return HttpResponse("<p> This is the index page </p>")

def home(request):
    context = {}
    return render(request, 'learninglog/home.html', context)

def places(request):
    page_title = 'The Places'
    context = { 'page_title': page_title }
    return render(request, 'learninglog/places.html', context)

def topics(request):
    topics = Topic.objects.all()
    # topics = Topic.objects.order_by('date_added')
    context = {'topics': topics }

    return render(request, 'learninglog/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    topic_entry = topic.entry_set.all()
    # topic_entry = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'topic_entry': topic_entry}

    return render(request, 'learninglog/topic.html', context)


def new_topic():
    pass

def new_entry():
    pass

def edit_entry():
    pass


# Create your views here.
