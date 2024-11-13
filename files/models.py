from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=50, verbose_name=("title"))
    body = RichTextField(default='', verbose_name=("body"))
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
