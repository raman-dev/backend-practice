#incrementing the answer count and total answers for a question
from django import forms
from .models import Answer,Question

class QuestionAnswerForm(forms.Form):
    answer = forms.ModelChoiceField(queryset=Answer.objects.none())
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def clean(self):
        # return super().clean()
        #make sure answer.question foreign key equals question
        cleaned_data = super().clean()
        answer = cleaned_data.get("answer")
        question = cleaned_data.get("question")
        if answer and question:
            if answer.question != question:
                raise forms.ValidationError("Answer does not belong to the question")
        return cleaned_data