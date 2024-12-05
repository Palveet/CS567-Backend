from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    political_affiliation = models.TextField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    ethnicity = models.TextField(null=True, blank=True)
    socioeconomic_status = models.TextField(null=True, blank=True)
    education_level = models.TextField(null=True, blank=True)
    occupation = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publisher = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    response = models.CharField(max_length=10)  # Yes/No
    created_at = models.DateTimeField(auto_now_add=True)
