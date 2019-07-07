from django.shortcuts import render
from .forms import CreatePost

# Create your views here.



def home(request):

    return render(request, 'home.html')

def createPost(request):
    form = CreatePost()
    msgg = 'hello'
    return render(request, 'createPost.html', {'form': form, 'msg':msgg})


def index(request):
    return render(request, 'index.html')
