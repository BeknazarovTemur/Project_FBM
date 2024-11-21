from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import active_languages_view
from languages.views import (
    AdminCatalogViewSet,
    LanguageViewSet,
    OriginalWordViewSet,
    UserLanguageWordViewSet,
)

router = DefaultRouter()
router.register("language-admin", LanguageViewSet, basename="language")
router.register("admin/catalog", AdminCatalogViewSet, basename="admin_catalog")
router.register("original-word", OriginalWordViewSet, basename="original_word")
router.register(
    "user/language-word", UserLanguageWordViewSet, basename="user_language_word"
)
urlpatterns = [
    path("", include(router.urls)),
    path('active/', active_languages_view, name='active_languages'),
]
