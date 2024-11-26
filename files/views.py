from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Prefetch
from languages.models import Language
from posts.models import Fact, Helpline, Link, Menu, MenuItem, Slider
from .models import Document
from django.utils.translation import get_language


# Create your views here.
class DocumentListView(ListView):
    model = Document
    template_name = 'download.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_language = get_language()

        documents = Document.objects.filter(is_active=True).order_by('-uploaded_at')[:4]
        documents_with_translations = []
        for document in documents:
            translation = document.translations.filter(language__code=current_language).first()
            if translation:
                documents_with_translations.append({
                    'title': translation.translated_title,
                    'body': translation.translated_body,
                    'file': document.file,
                    'uploaded_at': document.uploaded_at
                })
            else:
                documents_with_translations.append({
                    'title': document.title,
                    'body': document.body,
                    'file': document.file,
                    'uploaded_at': document.uploaded_at
                })
        
        context['documents'] = documents_with_translations
        context['sliders'] = Slider.objects.filter(is_active=True).all()
        context['links'] = Link.objects.filter(is_active=True).all()
        context['helplines'] = Helpline.objects.filter(is_active=True).all()
        context['menus'] = Menu.objects.filter(is_active=True).prefetch_related(Prefetch(
            'items',
            MenuItem.objects.filter(is_active=True)
        )).all()
        context['active_languages'] = Language.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        return Document.objects.filter(is_active=True).order_by('-uploaded_at')[:4]
    
def download_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    with open(document.file.path, 'rb') as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename="{document.file.name.split("/")[-1]}"'
        return response

def view_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return render(request, 'download.html', {'document': document})
