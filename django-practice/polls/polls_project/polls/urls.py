from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("login-page",views.login_page),
    path("login",views.login_request),
    path("logout",views.logout_request),
    path("submit-answer/<int:questionId>",views.submit_answer)
]