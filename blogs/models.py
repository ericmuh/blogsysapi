from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=30)
    subject = models.TextField(max_length=2000)
    author = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(max_length=450)
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.comment
