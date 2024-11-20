from django.urls import path
from .views import QuestionListView, QuestionAnswerDetailView
from .views import create_question


urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('question_form/', create_question, name='question_form'),
    path('question_answer/<int:pk>/', QuestionAnswerDetailView.as_view(), name='question_answer_detail'),
]
