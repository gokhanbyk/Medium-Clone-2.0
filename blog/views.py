from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def create_blog_post_view(request):
    form = BlogPostModelForm()
    context = dict(
        form = form
    )

    if request.method == 'POST':
        pass

    return render(request, 'blog/create_blog_post.html', context)