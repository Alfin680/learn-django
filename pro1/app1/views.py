from django.shortcuts import redirect, render
from django.contrib.auth.models import  User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    obj = Blog.objects.all()
    context = {
        'obj': obj,
    }
    return render(request, "home.html", context = context)

def regDetails(request):
    if request.method == 'POST':
        name = request.POST.get('u_name')
        passw = request.POST.get('pass')
        cpassw = request.POST.get('cpass')
        if passw == cpassw:
            data = User(username = name, password = passw)
            data.save()
        
    return redirect(index)

def blog_(request):
    if request.method == 'POST':
        titl = request.POST.get('title')
        cont = request.POST.get('content')
        data = Blog(title = titl, content = cont)
        data.save()
        return redirect(home)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username= username , password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return redirect(index)

def blog(request):
    return render(request, "blog.html")
    #return render(request, index.html)
# Create your views here.

def blogUpdate(request, pk):
    obj = Blog.objects.get(id = pk)
    context = {
        'obj': obj,
    }
    return render(request, "blogEdit.html", context = context)

def update(request, pk):
    if request.method == 'POST':
        Title = request.POST.get('edit_title')
        Content = request.POST.get('edit_content')

        dt = Blog.objects.get(id = pk)
        dt.title = Title
        dt.content = Content
        dt.save()
        return redirect(home)
    # else:
    #     return redirect(blogUpdate)


