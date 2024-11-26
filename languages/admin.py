from django.contrib import admin

from languages.models import Catalog, Language, OriginalWord, Translations


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "is_active"]
    search_fields = ["name", "code"]
    list_filter = ["is_active"]


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(OriginalWord)
class OriginalWordAdmin(admin.ModelAdmin):
    list_display = ["original_word", "catalog"]
    search_fields = ["original_word"]
    list_filter = ["catalog"]


@admin.register(Translations)
class TranslationsAdmin(admin.ModelAdmin):
    list_display = ["translation_text", "language", "original_word"]
    search_fields = ["translation_text"]
    list_filter = ["language"]
    raw_id_fields = ["original_word"]
    autocomplete_fields = ["original_word"]