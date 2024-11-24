from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from common.models import BaseModel


class Language(BaseModel):
    name = models.CharField(
        max_length=255, unique=True, verbose_name=_("Language Name")
    )
    code = models.CharField(max_length=10, unique=True, verbose_name=_("Language Code"))
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))

    def save(self, *args, **kwargs):
        if self.code == settings.DEFAULT_LANG:
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"

    def delete(self, using=None, keep_parents=False):
        if self.code == settings.DEFAULT_LANG:
            raise ValidationError("You can't delete this language")
        return super().delete(using, keep_parents)

    class Meta:
        db_table = "languages"
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
        ordering = ["-created_time"]


class Catalog(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Catalog Name"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "language_catalogs"
        verbose_name = _("Catalog")
        verbose_name_plural = _("Catalogs")
        ordering = ["-created_time"]


class OriginalWord(BaseModel):
    catalog = models.ForeignKey(
        "Catalog",
        on_delete=models.SET_NULL,
        related_name="original_words",
        null=True,
        blank=True,
        verbose_name=_("Catalog"),
    )
    original_word = models.TextField(unique=True, verbose_name=_("Original Word"))

    def __str__(self):
        return self.original_word

    class Meta:
        db_table = "original_words"
        verbose_name = _("Original Word")
        verbose_name_plural = _("Original Words")
        ordering = ["-created_time"]

    @property
    def translations(self):
        return self.translations.all()


class Translations(BaseModel):
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Language"),
    )
    original_word = models.ForeignKey(
        OriginalWord,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Original Word"),
    )
    translation_text = models.CharField(
        max_length=255, verbose_name=_("Translation Text")
    )

    def __str__(self):
        return f"{self.language} - {self.original_word}"

    class Meta:
        db_table = "translations"
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")
        ordering = ["-created_time"]
