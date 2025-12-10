from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    demo = models.CharField(max_length=50, default='demo')
class Blog(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    author = models.name = models.ForeignKey(Author, related_name='author', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)