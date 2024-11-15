from modeltranslation.translator import translator, TranslationOptions
from .models import Question

class QuestionTranslationOptions(TranslationOptions):
    fields = ('')

translator.register(Question, QuestionTranslationOptions)
