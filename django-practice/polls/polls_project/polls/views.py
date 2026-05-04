from django.shortcuts import render
from .models import Question,Answer

import random

def index(request):
    n = Question.objects.count()
    curr = random.randrange(0,n + 1)
    while not Question.objects.filter(id=curr).exists():
        curr = random.randrange(0,n + 1)

    randomQuestion = Question.objects.filter(id=curr).first() 
    context = {
        'question': randomQuestion,
        'answers': Answer.objects.filter(question=randomQuestion),
        'responses':randomQuestion.answered_count
    }

    return render(request,"polls/index.html",context=context)
