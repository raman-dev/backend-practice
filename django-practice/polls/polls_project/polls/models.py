from django.db import models


#
class Question(models.Model):
    value = models.CharField(default="Default Poll question",max_length=1024)
    responses = models.IntegerField(default=0,blank=True)
    
    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value
    

    class Meta:
        constraints = [models.UniqueConstraint(fields=["value"],name="unique_question")]

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    value = models.CharField(default="default answer",max_length=1024,unique=True)
    picked = models.IntegerField(default=0,blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["value","question"],name="unique_question_answer")]
    

    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value


"""
    Result of the poll is what?

    histogram of answers for a question
    add count field to answer 

    show results
"""