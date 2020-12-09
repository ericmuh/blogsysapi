from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["name", "subject", "author", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["comment", "blog", "owner", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Blog.objects.all(), required=False
    )
    comment = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Comment.objects.all(), required=False
    )

    class Meta:
        model = User
        fields = ["id", "username", "password", "blogs", "comment"]
