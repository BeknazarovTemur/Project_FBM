from django.db import models

from common.models import BaseModel


class Language(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        ordering = ["-created_at"]


class OriginalWord(BaseModel):
    catalog = models.ForeignKey(
        "Catalog",
        on_delete=models.SET_NULL,
        related_name="original_words",
        null=True,
        blank=True,
    )
    original_word = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_word

    class Meta:
        verbose_name = "Framework"
        verbose_name_plural = "Frameworks"
        ordering = ["-created_at"]


class Translations(BaseModel):
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="translations"
    )
    original_word = models.ForeignKey(
        OriginalWord, on_delete=models.CASCADE, related_name="translations"
    )
    translation_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.language} - {self.original_word}"

    class Meta:
        verbose_name = "Language Framework"
        verbose_name_plural = "Languages Frameworks"
        ordering = ["-created_at"]


class Catalog(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"
        ordering = ["-created_at"]
