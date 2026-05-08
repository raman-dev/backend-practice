from django.db import models
from django.contrib.auth.models import User

#
class Question(models.Model):
    value = models.CharField(default="Default Poll question",max_length=1024)
    responses = models.IntegerField(default=0,blank=True)
    respondents = models.ManyToManyField(User)
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
    need a seperate Response table
    to find what answer was give by what user to which question
"""

class Response(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    #ensure what 1 answer for 1 question by 1 user
    class Meta:
        constraints = [models.UniqueConstraint(fields=["question","user"],name="one_response_per_user_per_question")]

"""
    Result of the poll is what?

    histogram of answers for a question
    add count field to answer 

    show results
"""