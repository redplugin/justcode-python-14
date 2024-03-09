from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CreatePostForm
from blog.models import Post


# views - Представления
# templates - Шаблоны
# urls - ссылки


def test_view(request):
    return render(request, 'blog/test_view.html')


class PostListView(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


    # def get(self, request):
    #     posts = Post.objects.all().order_by('-created_at')
    #
    #     context = {
    #         'all_posts': posts
    #     }
    #
    #     return render(request, 'blog/index.html', context)


def index(request):  # PostListView
    posts = Post.objects.all().order_by('-created_at')
    # template = loader.get_template('blog/index.html')

    context = {
        'all_posts': posts
    }

    # return HttpResponse(template.render(context, request))

    return render(request, 'blog/index.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        return Post.objects.get(pk=post_id)


def detail(request, post_id):  # PostDetailView
    p = Post.objects.get(id=post_id)
    return HttpResponse(f"<h1> id: {p.id}. {p.title} </h1>"
                        f"<p> {p.content} test </p>")


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('index')
    form_class = CreatePostForm

    def form_valid(self, form):
        print("form instance", form.instance.id)
        form.instance.author_id = 1
        return super().form_valid(form)


def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.author_id = 1
            post.save()

            return redirect("index")
        else:
            return HttpResponse('Error creating!')

    # GET
    context = {
        'form': CreatePostForm()
    }

    return render(request,
                  'blog/create_post.html',
                  context=context)

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
