#incrementing the answer count and total answers for a question
from django import forms
from .models import Answer,Question

class QuestionAnswerForm(forms.Form):
    answer = forms.IntegerField()
    question = forms.IntegerField()

   

    def clean(self):
        # return super().clean()
        #make sure answer.question foreign key equals question
        cleaned_data = super().clean()
            
        answerId = self.cleaned_data.get("answer")
        questionId = self.cleaned_data.get("question")

        print(questionId,answerId)
        q = Question.objects.filter(id=questionId).first()
        a = Answer.objects.filter(question=q,id=answerId).first()

        print(q,a)
        if not q or not a:    
            raise forms.ValidationError("Invalid question or answer")
        
        if a.question != q:
            raise forms.ValidationError("Answer does not belong to question")
        
        return cleaned_data