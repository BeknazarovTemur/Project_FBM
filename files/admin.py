from django.contrib import admin
from files.models import Document

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'is_active')
    list_filter = ('title', 'uploaded_at')
    search_fields = ('title',)

admin.site.register(Document, DocumentAdmin)
