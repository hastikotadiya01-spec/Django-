from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import Contact
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    messages.success(request,"this is about")   
    return render(request,'home/about.html')    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  
        content = request.POST.get('content')
        
        if len(name) < 2 or len(email) < 3 or len(content) < 4 or (phone and len(phone) < 10):
            messages.error(request, "Please fill the form correctly")
            return redirect('contact')  
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            return redirect('contact')  

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET.get('query', '') 
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.error(request,"No search result found. Please refine your query")
    params ={'allPosts' : allPosts,'query' : query}
    return render(request,'home/search.html',params) 