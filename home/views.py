from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
from .models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
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
    query = request.GET.get('query',' ').strip()
    if len(query)>78:   
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.error(request,"No search result found . Please refine your query")
    params ={'allPosts' : allPosts,'query' : query}
    return render(request,'home/search.html',params) 

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if len(username)>10:
            messages.error(request,"Username must be under 10 character")
            return redirect('home') 
        
        if not username.isalnum():
            messages.error(request,"Username should only contains letters")
            return redirect('home')
        
        if pass1 != pass2 :
            messages.error(request,"password do not match")
            return redirect('home')
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname 
        myuser.last_name = lname 
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('home')
   
    else:
        return HttpResponse('handleSignup') 
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername , password=loginpassword)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials,PLease try again")
            return redirect('home')
                
    return HttpResponse('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('home') 