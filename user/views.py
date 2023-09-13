from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from slugify import slugify
from .models import Profile

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
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')

        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password) < 3:
            messages.warning(request, 'Bilgiler en az 3 karakterden oluşmalı')
            return redirect('user:register_view')
        if email != email_confirm:
            messages.warning(request, 'Lütfen email bilgisini doğru giriniz')
            return redirect('user:register_view')
        if password != password_confirm:
            messages.warning(request, 'Lütfen şifre bilgisini doğru giriniz')
            return redirect('user:register_view')
        
        user, created = User.objects.get_or_create(username = email) 
        if not created:
            user = authenticate(request, username = email, password = password)
            if user is not None:
                messages.success(request, 'Daha önce kayit olmuşsunuz.. Ana Sayfaya Yönlendirildiniz..')
                login(request, user)
                return redirect('home_view')
            messages.warning(request, f'{email} adresi sistemde kayitli ama login olmadiniz.. Login sayfasina yönlendiriliyorsunuz')
            return redirect('user:login_view')
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        
        profile, profile_created = Profile.objects.get_or_create(user = user)
        profile.instagram = instagram
        profile.slug = slugify(f'{first_name}-{last_name}')
        
        user.save()
        profile.save()

        messages.success(request, f'{user.first_name} sisteme kaydedildiniz..')
        user = authenticate(request, username = email, password = password)
        login(request, user)
        return redirect('home_view')

    context = dict()
    return render(request, 'user/register.html', context)