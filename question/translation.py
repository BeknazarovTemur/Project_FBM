from modeltranslation.translator import translator, TranslationOptions
from .models import Question

class QuestionTranslationOptions(TranslationOptions):
    fields = ('title', 'detail',)

translator.register(Question, QuestionTranslationOptions)
