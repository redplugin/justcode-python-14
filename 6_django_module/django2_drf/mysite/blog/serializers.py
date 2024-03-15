from django import forms
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'gender', 'demo_content']
        # fields = '__all__'
