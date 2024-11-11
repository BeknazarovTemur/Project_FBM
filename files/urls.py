from django.urls import path
from .views import DocumentListView
from . import views

urlpatterns = [
    path('download/', DocumentListView.as_view(), name='download'),
    path('download/<int:document_id>/', views.download_file, name='download_file'),
    path('view/<int:document_id>/', views.view_file, name='view_file'),
]
