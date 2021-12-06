from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from .forms import TopicForm, EntryForm
from .models import Topic
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

@login_required
def topics(request):
    topics = Topic.objects.all().order_by('date_added')

    context = {'topics':topics}

    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()

    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')
    context = {'form' :form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic',topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html',context )

@login_required
def edit_entry(request, entry_id):
    entry = Entry.object.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form - EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry, data=request.POST)
        if form.isvalid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)
    
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'MainApp/edit_entry.html',context)
