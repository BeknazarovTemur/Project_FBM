from django.shortcuts import render
from django.shortcuts import render, redirect
from appeal.models import Appeal
from files.models import Document
from posts.models import Link, Slider, Menu

# Create your views here.

def create_appeal(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        title = request.POST.get('title')
        message = request.POST.get('message')

        Appeal.objects.create(full_name=full_name, title=title, message=message)

        return redirect('home')
    
    menu_list = Menu.objects.all()
    document_list = Document.objects.all().order_by('-uploaded_at')[:4]
    slider_items = Slider.objects.all()
    link_items = Link.objects.all()
    context = {
        'menus': menu_list,
        'documents': document_list,
        'sliders': slider_items,
        'links': link_items,
    }
    return render(request, 'appeal_form.html', context)
