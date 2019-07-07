from django.shortcuts import render, redirect
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
            return redirect('/')
    else:
        form = CreatePost()
    return render(request, 'createPost.html', {'form': form})


def showPost(request, pk):
    post = Post.objects.get(id= pk)

    return render(request, 'post.html', {'post': post})

def index(request):
    return render(request, 'index.html')
