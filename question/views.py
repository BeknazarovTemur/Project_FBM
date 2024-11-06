from django.views.generic import ListView
from .models import Question
from django.shortcuts import render, redirect

# Create your views here.
class QuestionListView(ListView):
    model = Question
    template_name = 'question.html'

def create_question(request):
    if request.method == 'POST':
        number = request.POST.get('phone_number')
        title = request.POST.get('title')
        detail = request.POST.get('detail')

        Question.objects.create(number=number, title=title, detail=detail)

        return redirect('questions')
    return render(request, 'question_form.html')
