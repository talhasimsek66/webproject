from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forum.models import Comment
from django.contrib import messages

def home(request):
    return render(request, 'account_html/home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email address is already in use.')
            return render(request, 'account_html/register.html')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'account_html/register.html')
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('forum:home')  # Bu kısmı 'forum_home' gibi URL name olarak bırak
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')

    return render(request, 'account_html/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(user=request.user, content=content)
        return redirect('forum_page')
    return render(request, 'account_html/add_comment.html')
