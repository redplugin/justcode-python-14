from django.urls import path

from blog import views
from blog.views import PostListView, PostDetailView, PostCreateView

# localhost:8000/posts/
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('new/', PostCreateView.as_view(), name="create"),
    # path('test/', views.test_view),
    path('<int:post_id>/', PostDetailView.as_view(), name="detail"),
]

#  http://127.0.0.1:8000/blog/posts/?id=1
#  http://127.0.0.1:8000/blog/posts/2/