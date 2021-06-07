from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']

    @admin.display(description='Name')
    def question_text(self, obj):
        return obj.question_text.upper()


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
