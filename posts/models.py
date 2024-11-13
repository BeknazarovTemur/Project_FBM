from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=("category"))
    title = models.CharField(max_length=100, verbose_name=("title"))
    short_content = models.CharField(max_length=200, blank=True, verbose_name=("short_content"))
    content = RichTextField(verbose_name="content")
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    url = models.URLField(blank=True, null=True, verbose_name=_("URL"))

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='', verbose_name=_("Name"))
    url = models.URLField(blank=True, null=True, verbose_name=_("URL"))
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id'] 

class Slider(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, verbose_name=("title"))
    body = RichTextField(verbose_name=("body"))
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Link(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, verbose_name=("title"))
    def __str__(self):
        return self.title

class Fact(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, verbose_name="title")
    body = RichTextField(verbose_name=("body"))
    def __str__(self):
        return self.title

class Helpline(models.Model):
    head = models.CharField(max_length=200, default='', verbose_name="head")
    title = models.CharField(max_length=200, verbose_name=("title"))
    federation_title = models.CharField(max_length=200, default='', verbose_name=("federation_title"))
    federation_number = models.CharField(max_length=100, verbose_name=("federation_number"))
    state_title = models.CharField(max_length=200, default='', verbose_name=("state_title"))
    state_number = models.CharField(max_length=100, verbose_name=("state_number"))
    tag = models.CharField(max_length=200, default='', verbose_name=("tag"))
    def __str__(self):
        return self.title
    
class Call(models.Model):
    head = models.CharField(max_length=100, verbose_name=("head"))
    short_content = RichTextField(verbose_name=("short_content"))
    title = models.CharField(max_length=200, verbose_name=("title"))
    federation_content = models.CharField(max_length=200, default='', verbose_name=("federation_content"))
    federation_number = models.CharField(max_length=100, verbose_name=("federation_number"))
    state_content = models.CharField(max_length=200, verbose_name=("state_content"))
    state_number = models.CharField(max_length=100, verbose_name=("state_number"))
    def __str__(self):
        return self.title
