from django.urls import path

from . import views

# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # url from function based views
    # path("blogs/v1", views.blogs, name="blogs"),
    # path("blogs/v1/<int:pk>", views.blog_detail, name="blog-detail"),
    # urls from class based views
    # ! BLOGS
    path("blogs/", views.BlogList.as_view(), name="comments"),
    path("blogs/<int:pk>/", views.BlogDetail.as_view(), name="comment-detail"),
    # ! COMMENTS
    path("comments/", views.CommentList.as_view(), name="comments"),
    path("comments/<int:pk>/", views.CommentDetail.as_view(), name="comment-detail"),
    # ! USERS
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
