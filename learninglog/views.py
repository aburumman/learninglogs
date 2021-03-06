from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.views import logout, login
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render(request, 'learninglog/home.html', context)


@login_required
def topics(request):
    #topics = Topic.objects.all()
    topics = Topic.objects.filter(owner = request.user ).order_by('date_added')
    #if topics.owner != request.user:
        #raise Http404
    # topics = Topic.objects.order_by('date_added')
    context = {'topics': topics }

    return render(request, 'learninglog/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    topic_entry = topic.entry_set.all()
    if topic.owner != request.user:
        raise Http404
    # topic_entry = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'topic_entry': topic_entry}

    return render(request, 'learninglog/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid:
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learninglog:topics'))
    return render(request, 'learninglog/new_topic.html', {'form': form})


@login_required
def add_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
        if topic.owner != request.user:
            raise Http404
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid:
            add_entry = form.save(commit = False)
            add_entry.topic = topic
            add_entry.save()
            return HttpResponseRedirect(reverse('learninglog:topic', args=[topic_id]))
    context = {'form': form, 'topic': topic}
    return render(request, 'learninglog/add_entry.html', context)


@login_required
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
