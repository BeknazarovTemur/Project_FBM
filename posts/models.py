from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils import timezone
from languages.models import Language

# Create your models here.
    
class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    date = models.DateTimeField(null=True, blank=True,default=timezone.now)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _('Posts')
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

class PostTranslation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="translations")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=("title"))
    short_content = RichTextField(max_length=300, blank=True, verbose_name=("short_content"))
    content = RichTextField(verbose_name="content")

    class Meta:
        verbose_name = "Post Translation"
        verbose_name_plural = "Post Translations"
        unique_together = ('post', 'language')

    def __str__(self):
        return f"{self.post} ({self.language.name})"

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    url = models.URLField(blank=True, null=True, verbose_name=_("URL"))
    is_active = models.BooleanField(default=True, verbose_name="Is Active")


    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _('Menus')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='', verbose_name=_("Name"))
    url = models.URLField(blank=True, null=True, verbose_name=_("URL"))
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("MenuItem")
        verbose_name_plural = _('MenuItems')
        ordering = ['id']
    def __str__(self):
        return self.name



class Slider(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return f"Slider #{self.id}"

class SliderTranslation(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name="translations")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = RichTextField()

    class Meta:
        verbose_name = "Slider Translation"
        verbose_name_plural = "Slider Translations"
        unique_together = ('slider', 'language')

    def __str__(self):
        return f"{self.slider} ({self.language.name})"


class Link(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, verbose_name=("title"))
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _('Links')

    def __str__(self):
        return self.title

class Fact(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, verbose_name="title")
    body = RichTextField(verbose_name=("body"))
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = _("Fact")
        verbose_name_plural = _('Facts')

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
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = _("Helpline")
        verbose_name_plural = _('Helplines')

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
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = _("Call")
        verbose_name_plural = _('Calls')

    def __str__(self):
        return self.title
