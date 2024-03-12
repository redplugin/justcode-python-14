from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'POST':
        # print(request.POST)
        print(request.data)
        instance = PostSerializer(data=request.data)

        if instance.is_valid(raise_exception=True):
            instance.save()
            # post.author_id = 1
            # post.save()
            return Response(instance.data, status=status.HTTP_201_CREATED)
        # return Response({"detail": "Error creating", "status": status.HTTP_400_BAD_REQUEST})

    elif request.method == 'GET':
        post_id = request.GET.get('post_id')

        post = Post.objects.get(pk=post_id)

        if post:
            instance = PostSerializer(post)

            return Response(instance.data)
        return Response({"detail": "Post does not exist", "status": status.HTTP_404_NOT_FOUND})
