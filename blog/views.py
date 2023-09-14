from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
   
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.save()


    context = dict(
        form = form
    )
    return render(request, 'blog/create_blog_post.html', context)