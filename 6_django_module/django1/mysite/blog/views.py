from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request):
    return HttpResponse("Hello World!")


def posts(request):
    p = Post.objects.get(id=1)
    return HttpResponse(f"<h1> {p.title} </h1>"
                        f"<p> {p.content} </p>")

