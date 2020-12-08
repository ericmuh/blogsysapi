from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Comment.objects.all(),required=False
    )
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Blog
        fields = ["title", "subject", "author", "comments"]


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Comment
        fields = ["comment", "blog", "owner"]


class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all(),
required=False
)
    comments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Comment.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = ["id", "username", "password" "blogs", "comments"]
