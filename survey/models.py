from django.db import models

from user.models import User

class Question(models.Model):
    question      = models.CharField(max_length=256)
    sub_quesion   = models.CharField(max_length=256)
    user_question = models.ManyToManyField(User, through='UserQuestion', related_name = 'user_question')
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'questions'

class Answer(models.Model):
    answer      = models.CharField(max_length=256)
    question    = models.ForeignKey('Question', on_delete = models.SET_NULL, null=True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    answer_tag  = models.CharField(max_length = 256)
    answer_type = models.CharField(max_length = 100, null=True)

    class Meta:
        db_table = 'answers'

class UserQuestion(models.Model):
    user        = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    question    = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, related_name = 'questions')
    user_answer = models.IntegerField()

    class Meta:
        db_table = 'userquestions'

class Result(models.Model):
    name        = models.CharField(max_length=100)
    user_result = models.TextField(max_length=100000000)

    class Meta:
        db_table = 'results'
