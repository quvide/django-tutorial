"""
Django models for the polls application.

Models:
  Question
  Choice
"""

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Question model.

    Fields:
      question_text: Question title
      pub_date: Time published
      (choices as foreign keys)
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """Return question text for str()."""
        return self.question_text

    def was_published_recently(self):
        """Return true if question is less than a day old."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    """
    Choice model.

    Fields:
      question: Foreign key to Question
      choice_text: Choice text
    """

    question = models.ForeignKey(Question, related_name="choices",
                                 on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return choice text for str()."""
        return self.choice_text
