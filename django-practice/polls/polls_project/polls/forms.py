#incrementing the answer count and total answers for a question
from django import forms
from .models import Answer,Question, Response

class QuestionAnswerForm(forms.Form):
    answer = forms.IntegerField()
    question = forms.IntegerField()

   

    def clean(self):
        # return super().clean()
        #make sure answer.question foreign key equals question
        cleaned_data = super().clean()
            
        answerId = self.cleaned_data.get("answer")
        questionId = self.cleaned_data.get("question")

        q = Question.objects.filter(id=questionId).first()
        a = Answer.objects.filter(question=q,id=answerId).first()

        if not q or not a:    
            raise forms.ValidationError("Invalid question or answer")
        
        if a.question != q:
            raise forms.ValidationError("Answer does not belong to question")
        
        return cleaned_data


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields='__all__'
    
    def clean(self):
        cleaned_data = super().clean()
            
        a = self.cleaned_data.get("answer")
        q = self.cleaned_data.get("question")
        
        if not q or not a:    
            raise forms.ValidationError("Invalid question or answer")
        
        if a.question != q:
            raise forms.ValidationError("Answer does not belong to question")
        
        return cleaned_data
    