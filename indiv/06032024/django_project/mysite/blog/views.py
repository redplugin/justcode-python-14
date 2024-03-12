from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request):
    post = Post.objects.get(id=1)
    return HttpResponse(f"(id: {post.id})"
                        f"(title: {post.title})"
                        f"(content: {post.content})")
