from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Question(models.Model):
    number = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=300, verbose_name=("title"))
    detail = RichTextField(verbose_name=("detail"))
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

