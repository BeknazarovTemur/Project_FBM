from django.contrib import admin
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
    )

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Slider)
admin.site.register(Link)
admin.site.register(Fact)
admin.site.register(Helpline)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'is_active')
    list_filter = ('menu', 'parent', 'is_active')
    search_fields = ('name',)

admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Call)
