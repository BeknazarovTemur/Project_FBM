from modeltranslation.translator import translator, TranslationOptions
from .models import Document

class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(Document, DocumentTranslationOptions)
