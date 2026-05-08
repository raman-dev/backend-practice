from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

from .forms import QuestionAnswerForm
from .models import Question,Answer

import random

def index(request):
    n = Question.objects.count()
    curr = random.randrange(0,n + 1)
    while not Question.objects.filter(id=curr).exists():
        curr = random.randrange(0,n + 1)

    randomQuestion = Question.objects.filter(id=curr).first() 
    context= {
        'question': randomQuestion,
        'answers': Answer.objects.filter(question=randomQuestion),
    }

    return render(request,"polls/index.html",context=context)


def login_page(request):
    print("Login page requested")
    return render(request,"polls/login.html")

@require_POST
def login_request(request):

    # print(request)
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect("/")

    return JsonResponse({"error":"Unauthorized"},status=401)
    
    


@require_POST
def logout_request(request):
    logout(request)

    return redirect('/')

@login_required
@require_POST
def submit_answer(request,questionId):
    
    data = request.POST.copy()
    data['question'] = questionId
    
    print(data,type(data['answer']))
    qaForm = QuestionAnswerForm(data={'question':data['question'],'answer':int(data['answer'])})
    
    if qaForm.is_valid():
        #increment question answered count
        with transaction.atomic():
            question = Question.objects.filter(id=questionId).first()
            question.responses += 1
            question.save()
            #increment answer count
            answerId = qaForm.cleaned_data['answer']
            answer = Answer.objects.filter(id=answerId).first()
            answer.picked += 1
            answer.save()
        return redirect("/")
    else:
        print(qaForm.errors)    
    return JsonResponse({"message":"Invalid data"},status=400)