from django.contrib import admin
from .models import Question,Answer,Response


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["value","responses","id"]

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ["user","question","answer"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question__value","value","picked","id"]