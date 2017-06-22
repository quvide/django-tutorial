"""
Django models for the polls application.

Models:
  Question
  Choice
"""

import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(_("Question text"), max_length=200)
    pub_date = models.DateTimeField(_("Date published"))

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Return true if question is less than a day old."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = _("Published recently?")

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Choice(models.Model):
    """
    Choice model.

    Fields:
      question: Foreign key to Question
      choice_text: Choice text
      votes: Amount of votes
    """

    question = models.ForeignKey(Question, related_name="choices",
                                 on_delete=models.CASCADE)
    choice_text = models.CharField(_("Choice text"), max_length=200)
    votes = models.IntegerField(_("Votes"), default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")
