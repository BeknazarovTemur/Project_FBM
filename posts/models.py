from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100, default='')
    url = models.URLField(blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id'] 

class Slider(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Link(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Fact(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    def __str__(self):
        return self.title

class Helpline(models.Model):
    head = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    federation_title = models.CharField(max_length=200, default='')
    federation_number = models.CharField(max_length=100)
    state_title = models.CharField(max_length=200, default='')
    state_number = models.CharField(max_length=100)
    tag = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.title
    
class Call(models.Model):
    head = models.CharField(max_length=100)
    short_content = models.TextField()
    title = models.CharField(max_length=200)
    federation_content = models.CharField(max_length=200, default='')
    federation_number = models.CharField(max_length=100)
    state_content = models.CharField(max_length=200)
    state_number = models.CharField(max_length=100)
    def __str__(self):
        return self.title

