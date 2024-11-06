from django.urls import path
from appeal.views import create_appeal


urlpatterns = [
    path('appeal/', create_appeal, name = 'appeal_form')
]
