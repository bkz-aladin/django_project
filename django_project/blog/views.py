from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all
    return render(request, 'blog/index.html', {'posts' : posts})

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post' : post})
