from django.contrib import admin
from django.utils.html import strip_tags
from question.models import Question, QuestionAnswer

# Register your models here.

class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question_body', 'add_time', 'is_active')
    list_filter = ('question_body', 'add_time')
    search_fields = ('question_body',)

    def question_body(self, obj):
        return strip_tags(obj.question_body)
    question_body.short_description = "Question Body"

admin.site.register(Question)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)
