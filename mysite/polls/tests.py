import datetime
import pytest

from django.utils import timezone
from django.urls import reverse

from .models import Question

pytestmark = pytest.mark.django_db


class TestQuestionModel:

    def test_was_published_recently_with_future_question(self):
        # was_pulished_recently() must return False for questions whose pub
        # date is in the future
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        assert future_question.was_published_recently() is False


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(
        question_text=question_text, pub_date=time)


class TestQuestionIndexView:
    def test_no_questions(self, client):
        response = client.get(reverse("polls:index"))
        assert response.status_code == 200
        assert "No polls are available." in str(response.render().content)
        assert len(response.context["latest_question_list"]) == 0

    def test_past_question(self, client):
        create_question(question_text="Past question", days=-30)
        response = client.get(reverse("polls:index"))
        assert repr(response.context["latest_question_list"][0]) \
            == "<Question: Past question>"
        assert len(response.context["latest_question_list"]) == 1

    def test_future_question(self, client):
        """Ensure future questions are hidden from view"""
        create_question(question_text="Future question", days=30)
        response = client.get(reverse("polls:index"))
        assert "No polls are available." in str(response.render().content)
        assert len(response.context["latest_question_list"]) == 0


class TestQuestionDetailView:
    def test_future_question(self, client):
        """Ensure future questions are hidden from view"""
        future_question = create_question(question_text="Future question",
                                          days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = client.get(url)
        assert response.status_code == 404

    def test_past_question(self, client):
        """Ensure other questions show"""
        past_question = create_question(question_text="Past question", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = client.get(url)
        assert past_question.question_text in str(response.render().content)
