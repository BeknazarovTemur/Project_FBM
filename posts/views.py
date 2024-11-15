from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from files.models import Document
from question.models import Question
from .models import Fact, Helpline, Link, Call, Post, Slider, Menu, MenuItem
from django.db.models import Prefetch

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all().order_by('-uploaded_at')[:4]
        context['questions'] = Question.objects.all().order_by('-add_time')[:6]
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        context['menus'] = Menu.objects.prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all().order_by('-uploaded_at')[:4]  
        context['questions'] = Question.objects.all().order_by('-add_time')[:6]
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        context['menus'] = Menu.objects.prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        return context

class NewsListView(ListView):
    model = Post
    template_name = 'news.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all().order_by('-uploaded_at')[:4]
        context['questions'] = Question.objects.all().order_by('-add_time')[:6]
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        context['menus'] = Menu.objects.prefetch_related('items').all()
        return context

class CallListView(ListView):
    model = Post
    template_name = 'call.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all().order_by('-uploaded_at')[:4]
        context['questions'] = Question.objects.all().order_by('-add_time')[:6]
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        context['menus'] = Menu.objects.prefetch_related('items').all()
        context['calls'] = Call.objects.all()
        return context
