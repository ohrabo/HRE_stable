from django.shortcuts import render
from quiz.models import Quiz


def qpage(request):
	questions = Quiz.objects.all()
	answers = Quiz.objects.all().values('answer')

	return render(request, 'quiz/quiz_home.html', { 'questions': questions},
                  {'answers': answers}
                  )