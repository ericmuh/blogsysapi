from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Blog, Comment
from .permisions import IsOwnerOrReadOnly
from .serializers import BlogSerializer, CommentSerializer, UserSerializer

# Create your views here.

# ? Function based views
# gets all blogs and create blog

# !BLOG VIEWS
@api_view(["GET", "POST"])
def blogs(request):

    """
    List all blogs blogs, or create a new blog.
    """
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get a single blog, update a single blog and delete a single blog
@api_view(["GET", "PUT", "DELETE"])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code blog.
    """
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# ? Class based views


# ! BLOG VIEWS
class BlogList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,  IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer





# ! COMMENT VIEWS


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = CommentSerializer


# ! USER VIEWS
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
