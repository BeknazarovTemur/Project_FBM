from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'short_content', 'image',)
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class NewsListView(ListView):
    model = Post
    template_name = 'news.html'

class CallListView(ListView):
    model = Post
    template_name = 'call.html'

class DownloadListView(ListView):
    model = Post
    template_name = 'download.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
