from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm, BlogForm
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={"blogs": Blog.objects.all()})

def user_info(request):
    if request.method=="POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            blog = Blog(author=request.user,title=title, content=content)
            blog.save()
            return redirect('index')
        else:
            return render(request, 'blog/user.html', context={'username': request.user.username, "form": form})
    else:
        if request.user.is_authenticated:
            blogs = request.user.blogs.all()
            return render(request, 'blog/user.html', context={"username": request.user.username, "form": BlogForm(), "blogs": blogs})
        else:
            return redirect('log_in')
        

def sign_up(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('log_in')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', context={"form": form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'blog/login.html', context={"form": LoginForm()})
    return render(request, 'blog/login.html', context={"form": LoginForm()})

def log_out(request):
    logout(request)
    return redirect('index')

