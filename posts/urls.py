from django.urls import path
from .views import (
    PostDetailView, 
    PostListView, 
    NewsListView, 
    CallListView,
    )

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'), 
    path('call/', CallListView.as_view(), name='call'),
]