from django.shortcuts import render, redirect
from .form import CommentForm
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = Post.objects.all
    return render(request, 'blog/index.html', {'posts' : posts})


def show(request, id):
    post = Post.objects.get(id=id)  # This will handle 404 errors if the post is not found
    comments = post.comment_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)  # Instantiate the form with the POST data
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Set the comment's user to the currently logged-in user
            comment.save()
            return redirect('blog-show', id=post.id)  # Redirect to the same page to display the new comment
    else:
        form = CommentForm()

    return render(request, 'blog/post.html', {
        'post': post,
        'comments': comments,
        'form': form
    })