from django.urls import path
from .views import (
    PostDetailView, 
    PostListView, 
    NewsListView, 
    CallListView, 
    DownloadListView,
    PostUpdateView,
    PostDeleteView,

    )

urlpatterns = [
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_edit'),
    path('', PostListView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'), 
    path('call/', CallListView.as_view(), name='call'),
    path('download/', DownloadListView.as_view(), name='download'),
]