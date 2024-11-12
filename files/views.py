from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from posts.models import Fact, Helpline, Link, Menu, Slider
from .models import Document

# Create your views here.
class DocumentListView(ListView):
    model = Document
    template_name = 'download.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        context['sliders'] = Slider.objects.all()
        context['links'] = Link.objects.all()
        context['facts'] = Fact.objects.all()
        context['helplines'] = Helpline.objects.all()
        context['menus'] = Menu.objects.prefetch_related('items').all()
        return context

def download_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    with open(document.file.path, 'rb') as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename="{document.file.name.split("/")[-1]}"'
        return response

def view_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return render(request, 'download.html', {'document': document})
