from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    
    path("signup-page",views.signup_page),
    path("signup",views.register_request),
    path("success",views.signup_success),

    path("login-page",views.login_page),
    path("login",views.login_request),
    path("logout",views.logout_request),
    path("submit-answer/<int:questionId>",views.submit_answer)
]