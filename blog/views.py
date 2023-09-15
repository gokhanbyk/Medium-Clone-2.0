from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
import json


# Create your views here.

login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
   
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            tags_json = form.cleaned_data.get('tag')
            tags = json.loads(tags_json)
            for item in tags:
                value = item["value"]
                tag_item, created = Tag.objects.get_or_create(title=value)
                post.tag.add(tag_item)
            messages.success(request, 'Blog postunuz basariyla kaydedildi..')
            return redirect('home_view')

    context = dict(
        form = form
    )
    return render(request, 'blog/create_blog_post.html', context)