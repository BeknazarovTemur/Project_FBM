from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Menu, MenuItem, Slider, Link, Fact, Helpline, Call 

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'short_content', 'content',)

class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)

class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name',)

class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

class LinkTranslationOptions(TranslationOptions):
    fields = ('title',)

class FactTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

class HelplineTranslationOptions(TranslationOptions):
    fields = ('head', 'title', 'federation_title', 'state_title', 'tag',)

class CallTranslationOptions(TranslationOptions):
    fields = ('head', 'short_content', 'title', 'federation_content', 'state_content',)

translator.register(Post, PostTranslationOptions)
translator.register(Menu, MenuTranslationOptions)
translator.register(MenuItem, MenuItemTranslationOptions)
translator.register(Slider, SliderTranslationOptions)
translator.register(Link, LinkTranslationOptions)
translator.register(Fact, FactTranslationOptions)
translator.register(Helpline, HelplineTranslationOptions)
translator.register(Call, CallTranslationOptions)
