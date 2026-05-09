from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_GET
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import QuestionAnswerForm,ResponseForm
from .models import Question,Answer, Response

import random

def index(request):
    n = Question.objects.count()
    curr = random.randrange(0,n + 1)
    while not Question.objects.filter(id=curr).exists():
        curr = random.randrange(0,n + 1)

    randomQuestion = Question.objects.filter(id=curr).first() 

    answered = False 
    userAnswer = None
    if request.user and request.user.is_authenticated:
        # answered = randomQuestion.respondents.contains(request.user)
        response = Response.objects.filter(user=request.user,question=randomQuestion).first()
        if response:
            answered = True
            userAnswer = response.answer

    context= {
        'question': randomQuestion,
        'answers': Answer.objects.filter(question=randomQuestion),
        'answered': answered,
        'userAnswer': userAnswer
    }

    return render(request,"polls/index.html",context=context)


def login_page(request):
    print("Login page requested")
    return render(request,"polls/login.html")

@require_POST
def login_request(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request,user)
        print("Logged in")
        return redirect("/")

    return JsonResponse({"error":"Unauthorized"},status=401)

@require_GET
def signup_page(request):
    return render(request,"polls/signup.html")

@require_POST
def register_request(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    if User.objects.filter(username=username).exists():
        #return an error
        return redirect("/signup")
    ucf = UserCreationForm(data={
        'username':username,
        'password1':password,
        'password2':password
    })
    if not ucf.is_valid():
        print(ucf.errors)
        return redirect("/signup")
    ucf.save()
    return redirect("/success")

@require_GET
def signup_success(request):
    return render(request,"polls/success.html")

@require_POST
def logout_request(request):
    logout(request)

    return redirect('/')

@login_required
@require_POST
def submit_answer(request,questionId):
    
    #get user object
    data = request.POST.copy()
    data['question'] = questionId
    
    # qaForm = QuestionAnswerForm(data={'question':data['question'],'answer':int(data['answer'])})
    
    user = request.user
    rf = ResponseForm(data={
        'user':user,
        'question':data['question'],
        'answer':int(data['answer'])})
    if rf.is_valid():#qaForm.is_valid():
        #increment question answered count
        with transaction.atomic():
            response = rf.save()

            question = response.question
            question.responses += 1
            question.save()
            #increment answer count
            answer = response.answer
            answer.picked += 1
            answer.save()
        return redirect("/")
    else:
        # print(qaForm.errors)
        print(rf.errors)    
        return redirect('/')
    return JsonResponse({"message":"Invalid data"},status=400)