from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from files.models import Document
from languages.models import Language
from question.models import QuestionAnswer
from .models import Fact, Helpline, Link, Call, Post, Slider, Menu, MenuItem
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all().order_by('-uploaded_at')[:4]
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['facts'] = Fact.objects.filter(is_active=True).all()
        context['helplines'] = Helpline.objects.filter(is_active=True).all()
        context['question_answers'] = QuestionAnswer.objects.filter(is_active=True).all().order_by('-add_time')[:6]
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(is_active=True).all().order_by('-uploaded_at')[:4]  
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['helplines'] = Helpline.objects.filter(is_active=True).all()
        context['question_answers'] = QuestionAnswer.objects.filter(is_active=True).all().order_by('-add_time')[:6]
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)

        return context

class NewsListView(ListView):
    model = Post
    template_name = 'news.html'
    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(is_active=True).all().order_by('-uploaded_at')[:4]
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['facts'] = Fact.objects.filter(is_active=True).all()
        context['helplines'] = Helpline.objects.filter(is_active=True).all()
        context['question_answers'] = QuestionAnswer.objects.filter(is_active=True).all().order_by('-add_time')[:6]
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)
        return context

class CallListView(ListView):
    model = Post
    template_name = 'call.html'
    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('-date')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(is_active=True).all().order_by('-uploaded_at')[:4]
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['facts'] = Fact.objects.filter(is_active=True).all()
        context['helplines'] = Helpline.objects.filter(is_active=True).all()
        context['question_answers'] = QuestionAnswer.objects.filter(is_active=True).all().order_by('-add_time')[:6]
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)
        context['calls'] = Call.objects.filter(is_active=True).all()
        return context
