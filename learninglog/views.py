from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('learninglog:topics'))
    return render(request, 'learninglog/new_topic.html', {'form': form})


def add_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid:
            add_entry = form.save(commit = False)
            add_entry.topic = topic
            add_entry.save()
            return HttpResponseRedirect(reverse('learninglog:topic', args=[topic_id]))
    context = {'form': form, 'topic': topic}
    return render(request, 'learninglog/add_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance = entry)

    else:
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            #entry = form.save(commit = FALSE)
            #entry.topic = topic
            form.save()
            return HttpResponseRedirect(reverse('learninglog:topic', args=[topic.id]))

    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learninglog/edit_entry.html', context)




# Create your views here.
