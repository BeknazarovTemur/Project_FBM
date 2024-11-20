from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags

# Create your models here.
class Question(models.Model):
    number = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=300, default="")
    detail = RichTextField(verbose_name=("detail"), default="")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.title

class QuestionAnswer(models.Model):
    question_body = RichTextField(verbose_name=("question body"))
    answer_body = RichTextField(verbose_name=("answer body"))
    add_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    def save(self, *args, **kwargs):
        self.question_body = strip_tags(self.question_body)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Question Asnswer")
        verbose_name_plural = _('Questions Answers')
    
    def __str__(self):
        return self.question_body
