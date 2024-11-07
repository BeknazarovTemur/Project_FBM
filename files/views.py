from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Document

# Create your views here.
class DocumentListView(ListView):
    model = Document
    template_name = 'download.html'

def download_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    with open(document.file.path, 'rb') as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename="{document.file.name.split("/")[-1]}"'
        return response

def view_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return render(request, 'download.html', {'document': document})
