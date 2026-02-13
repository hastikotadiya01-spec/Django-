from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, BlogComment
from django.contrib import messages

def blogHome(request):
    posts = Post.objects.all()
    return render(request, "blog/blogHome.html", {'posts': posts})

def blogPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = BlogComment.objects.filter(post=post).order_by('timestamp')  
    context = {'post': post, 'comments': comments}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = get_object_or_404(Post, sno=postSno)                      
        comment = BlogComment(comment=comment_text, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        return redirect(f"/blog/blogpost/{post.slug}/")
    return redirect("/blog/")
