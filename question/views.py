from django.views.generic import ListView
from files.models import Document
from posts.models import Fact, Link, Menu, Slider
from .models import Question
from django.shortcuts import render, redirect

# Create your views here.
class QuestionListView(ListView):
    model = Question
    template_name = 'question.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['menus'] = Menu.objects.prefetch_related('items').all()
        return context

def create_question(request):
    if request.method == 'POST':
        number = request.POST.get('phone_number')
        title = request.POST.get('title')
        detail = request.POST.get('detail')

        Question.objects.create(number=number, title=title, detail=detail)

        return redirect('questions')
    menu_list = Menu.objects.all()
    document_list = Document.objects.all()
    slider_items = Slider.objects.all()
    link_items = Link.objects.all()
    context = {
        'menus': menu_list,
        'documents': document_list,
        'sliders': slider_items,
        'links': link_items,
    }
    return render(request, 'question_form.html', context)
