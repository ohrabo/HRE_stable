from django.contrib import admin

from quiz.models import Quiz, Category

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}