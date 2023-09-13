from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username}Daha önce login olmuşsun')
        return redirect('home_view')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Login Oldun')
            return redirect('home_view')

    context = dict()
    return render(request, 'user/login.html', context)

def logout_view(request):
    pass