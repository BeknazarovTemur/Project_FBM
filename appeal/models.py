from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Appeal(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    message = RichTextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Appeal")
        verbose_name_plural = _('Appeals')

    def __str__(self):
        return self.title
