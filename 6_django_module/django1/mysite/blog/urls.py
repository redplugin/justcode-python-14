from django.urls import path

from blog.views import index, posts

urlpatterns = [
    path('', index),
    path('post/', posts)
]

