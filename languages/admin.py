from django.contrib import admin
from .models import Catalog, Language, OriginalWord, Translations


from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Catalog, Language, OriginalWord, Translations


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    ordering = ("id",)


@admin.register(Language)
class LanguageAdmin(BaseAdmin):
    list_display = ("id", "name", "code", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "code")
    list_display_links = ("id",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('languages-admin/', self.languages_admin_view, name='languages_admin'),
        ]
        return custom_urls + urls

    def languages_admin_view(self, request):
        languages = Language.objects.all()
        context = {
            'languages': languages,
            'opts': self.model._meta,
        }
        return render(request, 'languages/languages_admin.html', context)


class TranslationsInline(admin.TabularInline):
    model = Translations
    extra = 1
    fields = ("language", "translation_text")
    readonly_fields = ("id",)


@admin.register(OriginalWord)
class OriginalWordAdmin(BaseAdmin):
    list_display = ("id", "original_word", "get_catalog")
    search_fields = (
        "original_word",
        "catalog__name",
    )
    list_filter = ("catalog__name",)
    list_display_links = ("id",)

    def get_catalog(self, instance):
        return instance.catalog.name

    get_catalog.short_description = "Catalog"
    inlines = [TranslationsInline]


@admin.register(Catalog)
class CatalogAdmin(BaseAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ()
    search_fields = ("name",)
    list_display_links = ("id",)
