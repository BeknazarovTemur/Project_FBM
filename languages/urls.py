from django.urls import path
from . import views

urlpatterns = [
    path('translations/', views.ListTranslationsView.as_view(), name='list_translations'),
    path('languages/', views.LanguageListView.as_view(), name='language_list'),
    path('original-words/', views.OriginalWordListView.as_view(), name='original_word_list'),
    path('user-language-words/', views.UserLanguageWordListView.as_view(), name='user_language_word_list'),
    path('catalogs/', views.CatalogListView.as_view(), name='catalog_list'),
]
