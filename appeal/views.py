from django.shortcuts import render
from django.shortcuts import render, redirect
from appeal.models import Appeal

# Create your views here.

def create_appeal(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        title = request.POST.get('title')
        message = request.POST.get('message')

        Appeal.objects.create(full_name=full_name, title=title, message=message)

        return redirect('home')
    return render(request, 'appeal_form.html')
