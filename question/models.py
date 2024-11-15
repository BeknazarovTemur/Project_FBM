from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Question(models.Model):
    number = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=300)
    detail = RichTextField(verbose_name=("detail"))
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.title

