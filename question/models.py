from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    number = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=300)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

