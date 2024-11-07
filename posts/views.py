from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from files.models import Document
from question.models import Question
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all() 
        context['questions'] = Question.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        return context

class NewsListView(ListView):
    model = Post
    template_name = 'news.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['questions'] = Question.objects.all()
        return context

class CallListView(ListView):
    model = Post
    template_name = 'call.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['questions'] = Question.objects.all()
        return context
