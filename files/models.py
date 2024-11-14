from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _



# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=50, verbose_name=("title"))
    body = RichTextField(default='', verbose_name=("body"))
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _('Documents')

    def __str__(self):
        return self.title
