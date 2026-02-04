
from django.shortcuts import render, get_object_or_404
from .models import Post

def blogHome(request):
    posts = Post.objects.all()
    return render(request, "blog/blogHome.html", {'posts': posts})

def blogPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/blogPost.html", {'post': post})

