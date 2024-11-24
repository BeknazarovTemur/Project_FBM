from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Language, OriginalWord, Translations

def list_translations(request):
    translations = Translations.objects.select_related('language', 'original_word')
    data = [
        {
            "id": translation.id,
            "language": translation.language.name,
            "original_word": translation.original_word.original_word,
            "translation_text": translation.translation_text,
        }
        for translation in translations
    ]
    return JsonResponse(data, safe=False)

def translation_detail(request, pk):
    translation = get_object_or_404(Translations, pk=pk)
    data = {
        "id": translation.id,
        "language": translation.language.name,
        "original_word": translation.original_word.original_word,
        "translation_text": translation.translation_text,
    }
    return JsonResponse(data)

def create_translation(request):
    if request.method == "POST":
        language_id = request.POST.get("language_id")
        original_word_id = request.POST.get("original_word_id")
        translation_text = request.POST.get("translation_text")

        language = get_object_or_404(Language, pk=language_id)
        original_word = get_object_or_404(OriginalWord, pk=original_word_id)

        translation = Translations.objects.create(
            language=language,
            original_word=original_word,
            translation_text=translation_text,
        )
        data = {
            "id": translation.id,
            "language": translation.language.name,
            "original_word": translation.original_word.original_word,
            "translation_text": translation.translation_text,
        }
        return JsonResponse(data, status=201)
    return JsonResponse({"error": "Invalid method"}, status=400)
