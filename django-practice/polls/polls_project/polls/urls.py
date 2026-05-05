from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("login",views.login_page),
    path("submit-answer",views.submit_answer)
]