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

        if len(username) < 6 or len(password) < 6:
            messages.warning(request, f'lütfen kullanici adi veya sifreyi dogru giriniz.. 6 karakterden küçük olamaz')
            return redirect('user:login_view')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Login Oldun')
            return redirect('home_view')

    context = dict()
    return render(request, 'user/login.html', context)

def logout_view(request):
    messages.info(request, f'{request.user.username} Oturum Kapatıldı')    
    logout(request)
    return redirect('home_view')   

def register_view(request):
    if request.method == 'POST':
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_Name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')

        


    context = dict()
    return render(request, 'user/register.html', context)