# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField('the question', max_length=250)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
    
    def __unicode__(self):  # __str__ on Python 3
        return self.question_text
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField('the answer', max_length=250)
    votes = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.answer_text 