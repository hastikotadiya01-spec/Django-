
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Post , BlogComment
from django.contrib import messages 

def blogHome(request):
    posts = Post.objects.all()
    return render(request, "blog/blogHome.html", {'posts': posts})

def blogPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = BlogComment.objects.filter(post=post)
    return render(request, "blog/blogPost.html", {'post': post})

def postComment(request, slug):
    if request.method=='POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post =  Posts.objects.get(sno=postSno)
        comment = BlogComment(comment=comment ,user=user , post=post)
        comment.save()
        messages.success(request,"your comment has been posted successfully")
    
    return redirect(f"/blog/{post.slug}")    
     
        
        