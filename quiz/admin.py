from django.contrib import admin

from quiz.models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

