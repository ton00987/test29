from django.db import models

# Create your models here.
class Quiz(models.Model):
    ques = models.TextField(default='')
    ans = models.BooleanField()