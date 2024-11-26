from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import F
from languages.models import Catalog, Language, OriginalWord


class ListTranslationsView(View):
    def get(self, request):
        translations = OriginalWord.objects.all()
        data = [{"id": word.id, "original_word": word.original_word} for word in translations]
        return JsonResponse(data, safe=False)


class LanguageListView(View):
    def get(self, request):
        languages = Language.objects.all()
        data = [{"id": lang.id, "name": lang.name, "code": lang.code} for lang in languages]
        return JsonResponse(data, safe=False)


class OriginalWordListView(View):
    def get(self, request):
        words = OriginalWord.objects.all()
        data = [{"id": word.id, "original_word": word.original_word} for word in words]
        return JsonResponse(data, safe=False)


class UserLanguageWordListView(View):
    def get(self, request):
        language = self.request.headers.get("Accept-Language")
        if (
            not language
            or not Language.objects.filter(code=language, is_active=True).exists()
        ):
            return JsonResponse([], safe=False)
        words = OriginalWord.objects.filter(translations__language__code=language).annotate(
            translation_text=F("translations__translation_text")
        )
        data = [{"id": word.id, "original_word": word.original_word, "translation_text": word.translation_text} for word in words]
        return JsonResponse(data, safe=False)


class CatalogListView(View):
    def get(self, request):
        catalogs = Catalog.objects.all()
        data = [{"id": catalog.id, "name": catalog.name} for catalog in catalogs]
        return JsonResponse(data, safe=False)
