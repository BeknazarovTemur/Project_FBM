from django.urls import path
from .views import list_translations, translation_detail, create_translation

urlpatterns = [
    path('translations/', list_translations, name='list_translations'),
    path('translations/<int:pk>/', translation_detail, name='translation_detail'),
    path('translations/create/', create_translation, name='create_translation'),
]
