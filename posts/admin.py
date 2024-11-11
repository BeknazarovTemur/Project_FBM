from django.contrib import admin
from posts.models import (
    Category, 
    Fact, 
    Helpline, 
    Link, 
    MenuItem,
    Post, 
    Slider,
    )

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Slider)
admin.site.register(Link)
admin.site.register(Fact)
admin.site.register(Helpline)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'parent', 'is_active']
    list_filter = ['parent', 'is_active']
    search_fields = ['name', 'url']

admin.site.register(MenuItem, MenuItemAdmin)
