from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from languages.filters import WordsFilterSet
from languages.models import Catalog, Language, OriginalWord
from django.shortcuts import render

def active_languages_view(request):
    languages = Language.objects.filter(is_active=True)
    return render(request, 'languages/active_languages.html', {'languages': languages})

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_active"]
    pagination_class = None
    authentication_classes = []


class OriginalWordViewSet(ModelViewSet):
    queryset = OriginalWord.objects.all()
    permission_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WordsFilterSet
    search_fields = ["original_word", "translations__translation_text"]
    ordering_fields = ["original_word", "translations"]
    authentication_classes = []
    

class UserLanguageWordViewSet(ListModelMixin, GenericViewSet):
    queryset = OriginalWord.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WordsFilterSet
    pagination_class = None
    authentication_classes = []

    def get_queryset(self):
        language = self.request.headers.get("Accept-Language")
        if (
            not language
            or not Language.objects.filter(code=language, is_active=True).exists()
        ):
            return self.queryset.none()
        return self.queryset.filter(translations__language__code=language).annotate(
            translation_text=F("translations__translation_text")
        )


class AdminCatalogViewSet(ModelViewSet):
    queryset = Catalog.objects.all()
    permission_classes = [AllowAny]
    pagination_class = None
    authentication_classes = []
