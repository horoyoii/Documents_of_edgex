from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import copy
# Create your views here.



def home(request):

    return render(request, 'home.html')

def createPost(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/content_list')
    else:
        form = CreatePost()
    return render(request, 'createPost.html', {'form': form})

def content_edit(request, pk):
    item = get_object_or_404(Post, id=pk)
    form = CreatePost(request.POST or None, instance=item)
    if(form.is_valid()):
        form.save()
        return redirect('/content_list')
    return render(request, 'createPost.html', {'form': form})


def content_delete(request, pk):
    item = Post.objects.get(id=pk)
    item.delete()
    return redirect('/content_list')

def showPost(request, pk):
    post = Post.objects.get(id= pk)

    return render(request, 'post.html', {'post': post})

def index(request):
    done_list = Done.objects.all()

    
    return render(request, 'index.html', {'done_list':done_list})


def content_list(request):
    #post_title = Post.objects.values_list('title', 'id')
    
    posts = Post.objects.all().order_by('number') 
    liss = {}
    sub =[]
    flag= False
    key_str = ""
    for p in posts:
        if p.number.count('.') == 1 and flag:
            liss[key_str] = sub
            sub=[]
            key_str = p.number+" "+p.title
            #sub.append(p)
        else:
            sub.append(p)

        if not flag:
            sub=[]
            key_str = p.number+" "+p.title
            flag=True
    liss[key_str]=sub
    
    tag = ['abc', 'bcd', 'kkk','acc']

    ab=zip(tag, liss.items())

    return render(request, 'content_list.html', {'posts':posts, 'liss':ab})

def content_main(request, pk):
    post_all = Post.objects.all().order_by('number')
    post = Post.objects.get(id=pk)
    print(post_all)
    print(post)
    return render(request, 'content_main.html', {'post':post, 'post_all': post_all})

def createDone(request):
    if request.method == "POST":
        form = CreateDone(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/content_list')
    else:
        form = CreateDone()
    return render(request, 'createPost.html', {'form': form})

def done_edit(request, pk):
    item = get_object_or_404(Done, id=pk)
    form = CreateDone(request.POST or None, instance=item)
    if(form.is_valid()):
        form.save()
        return redirect('/index')
    return render(request, 'createPost.html', {'form': form})


def done_delete(request, pk):
    item = Done.objects.get(id=pk)
    item.delete()
    return redirect('/index')
