from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePost
from .models import *
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
    return render(request, 'index.html')


def content_list(request):
    #post_title = Post.objects.values_list('title', 'id')
    post_title = Post.objects.all().order_by('number') 
    print(post_title)


    return render(request, 'content_list.html', {'post_title':post_title})

def content_main(request, pk):
    post_all = Post.objects.all().order_by('number')
    post = Post.objects.get(id=pk)
    print(post_all)
    print(post)
    return render(request, 'content_main.html', {'post':post, 'post_all': post_all})
