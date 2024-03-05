from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from blog.models import Post

# views - Представления
# templates - Шаблоны
# urls - ссылки


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    # template = loader.get_template('blog/index.html')

    context = {
        'all_posts': posts
    }

    # return HttpResponse(template.render(context, request))

    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    p = Post.objects.get(id=post_id)
    return HttpResponse(f"<h1> id: {p.id}. {p.title} </h1>"
                        f"<p> {p.content} test </p>")


# def posts(request):
#     post_id = request.GET.get('id', 1)
#     p = Post.objects.get(id=post_id)
#     return HttpResponse(f"<h1> id: {p.id}. {p.title} </h1>"
#                         f"<p> {p.content} test </p>")

# def index(request):
#     posts = Post.objects.all().order_by('-created_at')
#     response = (f"<ul>"
#                 f"{ ''.join([f'<li>{post.title}</li>' for post in posts]) }"
#                 f"</ul>")
#     return HttpResponse(response)