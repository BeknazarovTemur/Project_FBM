from django.views.generic import ListView, DetailView
from files.models import Document
from languages.models import Language
from posts.models import Link, Menu, MenuItem, Slider
from .models import Question, QuestionAnswer
from django.shortcuts import render, redirect
from django.db.models import Prefetch

# Create your views here.
class QuestionListView(ListView):
    model = Question
    template_name = 'question.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(is_active=True).all().order_by('-uploaded_at')[:4]
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)
        return context
    def get_queryset(self):
        return Question.objects.all().order_by('-add_time')[:6]

def create_question(request):
    if request.method == 'POST':
        number = request.POST.get('phone_number')
        title = request.POST.get('title')
        detail = request.POST.get('detail')

        Question.objects.create(number=number, title=title, detail=detail)

        return redirect('questions')
    menu_list = Menu.objects.all()
    document_list = Document.objects.all()
    question_list = Question.objects.all().order_by('-add_time')[:6]
    slider_items = Slider.objects.all()
    link_items = Link.objects.all()
    context = {
        'menus': menu_list,
        'documents': document_list,
        'questions': question_list,
        'sliders': slider_items,
        'links': link_items,
    }
    context['active_languages'] = Language.objects.filter(is_active=True)
    return render(request, 'question_form.html', context)

class QuestionAnswerListView(ListView):
    model = QuestionAnswer
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(is_active=True).all().order_by('-uploaded_at')[:4]
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['question_answers'] = QuestionAnswer.objects.filter(is_active=True).order_by('-add_time')[:6]
        context['active_languages'] = Language.objects.filter(is_active=True)
        return context

class QuestionAnswerDetailView(DetailView):
    model = QuestionAnswer
    template_name = 'answer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(is_active=True).all().order_by('-uploaded_at')[:4]
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)
        return context
