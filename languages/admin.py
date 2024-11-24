from django.contrib import admin
from .models import Language, Catalog, OriginalWord, Translations

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created_time')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')
    ordering = ['-created_time']

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')
    search_fields = ('name',)
    ordering = ['-created_time']

@admin.register(OriginalWord)
class OriginalWordAdmin(admin.ModelAdmin):
    list_display = ('original_word', 'catalog', 'created_time')
    list_filter = ('catalog',)
    search_fields = ('original_word',)
    ordering = ['-created_time']

@admin.register(Translations)
class TranslationsAdmin(admin.ModelAdmin):
    list_display = ('language', 'original_word', 'translation_text', 'created_time')
    list_filter = ('language', 'original_word')
    search_fields = ('translation_text',)
    ordering = ['-created_time']
