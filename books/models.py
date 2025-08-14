from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_reviews")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to="books/", blank=True, null=True)
    ai_summary = models.TextField(blank=True, null=True)
    ai_pros = models.TextField(blank=True, null=True)
    ai_cons = models.TextField(blank=True, null=True)
    ai_score = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    decision = models.CharField(
        max_length=10,
        choices=[("pending", "Pending"), ("read", "Read"), ("skip", "Skip")],
        default="pending"
    )
    
