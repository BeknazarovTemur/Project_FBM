from django.contrib import admin
from django import forms
from django.contrib import admin
from languages.models import Language
from posts.models import (
    Category, 
    Fact, 
    Helpline, 
    Link, 
    Menu,
    MenuItem,
    Post, 
    Slider,
    Call,
    SliderTranslation,
    )

# Register your models here.

admin.site.register(Category)

class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'date', 'created_at','is_active')
    list_filter = ('title', 'short_content', 'created_at')
    search_fields = ('title',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "language":
            kwargs["queryset"] = Language.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active')
    list_filter = ('name', 'url')
    search_fields = ('name',)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'is_active')
    list_filter = ('menu', 'parent', 'is_active')
    search_fields = ('name',)

class SliderTranslationInline(admin.TabularInline):
    model = SliderTranslation
    extra = 0
    fields = ('language', 'title', 'body')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "language":
            kwargs["queryset"] = Language.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'created_at')
    list_filter = ('is_active',)
    inlines = [SliderTranslationInline]


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('title', 'is_active')
    search_fields = ('title',)

class FactAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('title', 'is_active')
    search_fields = ('title',)

class HelplineAdmin(admin.ModelAdmin):
    list_display = ('title', 'federation_number', 'state_number', 'is_active')
    list_filter = ('title', 'federation_number', 'state_number', 'is_active')
    search_fields = ('title',)

class CallAdmin(admin.ModelAdmin):
    list_display = ('title', 'federation_number', 'state_number', 'is_active')
    list_filter = ('title', 'federation_number', 'state_number', 'is_active')
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Helpline, HelplineAdmin)
admin.site.register(Call, CallAdmin)
