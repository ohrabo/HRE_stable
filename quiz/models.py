from django.db import models

from map.models import Category


class Quiz(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length = 1020)
    option1 = models.CharField(max_length = 420)
    option2 = models.CharField(max_length = 420)
    option3 = models.CharField(max_length = 420, null=True)
    option4 = models.CharField(max_length = 420, null=True)
    answer = models.IntegerField(help_text="Enter the number of the correct option")

    def __str__(self):
        return self.question
