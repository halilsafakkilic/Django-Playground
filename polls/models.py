import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    STATUS = (
        ('0', 'Passive'),
        ('1', 'Active'),
    )

    question_text = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=1, default=0, choices=STATUS)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return "{}:{}..".format(self.id, self.question_text[:10])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
