from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    
    context = dict()
    return render(request, 'user/login.html', context)

