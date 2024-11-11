from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from files.models import Document
from question.models import Question
from .models import Fact, Helpline, Link, MenuItem, Post, Slider

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all() 
        context['questions'] = Question.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        return context
    
    def nav_view(request):
        top_level_items = MenuItem.objects.filter(parent__isnull=True)
        context = {
            'menu_items': top_level_items
        }
        return render(request, 'base.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['questions'] = Question.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        return context

class NewsListView(ListView):
    model = Post
    template_name = 'news.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['questions'] = Question.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        return context

class CallListView(ListView):
    model = Post
    template_name = 'call.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['questions'] = Question.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        return context
