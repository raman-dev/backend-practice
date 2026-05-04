from django.contrib import admin
from .models import Question,Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["value","answered_count"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question__value","value","picked"]