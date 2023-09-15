from django.urls import path
from .views import *

app_name = 'read'

urlpatterns = [
    path('<slug:user_slug>/', all_posts_view, name='all_posts_view'),
]
