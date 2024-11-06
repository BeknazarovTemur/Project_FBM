from django.urls import path
from .views import QuestionListView
from .views import create_question


urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('question_form/', create_question, name='question_form')
]
