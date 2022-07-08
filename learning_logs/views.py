from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404
from django.contrib.auth.decorators import login_required

# help functions:

def check_object_owner(place, request):
    """Checks if user is object owner"""

    if place.owner != request.user:
        raise Http404

# All  views :

def index(request):
    """Welcome page"""

    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Shows list of topics"""

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Renders topic page"""

    topic = get_object_or_404(Topic, id=topic_id)
    check_object_owner(topic, request)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Renders topic creation page"""

    if request.method != 'POST':
        form = TopicForm()
    else:  
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Renders entry creation page"""
    
    topic = get_object_or_404(Topic, id=topic_id)
    check_obejct_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Renders entry edit page"""

    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    check_object_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
