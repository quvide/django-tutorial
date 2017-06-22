import datetime
import pytest
from freezegun import freeze_time

from django.utils import timezone
from django.urls import reverse

from .models import Question

pytestmark = pytest.mark.django_db


@freeze_time("2017-01-01")
def create_question(question_text, days):
    # helper function
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(
        question_text=question_text, pub_date=time)


class TestQuestionModel:

    @freeze_time("2017-01-01")
    def test_was_published_recently_with_future_question(self):
        """Ensure questions in the future are not 'recently published'."""
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        assert future_question.was_published_recently() is False


class TestQuestionIndexView:

    def test_no_questions(self, client):
        """Ensure empty index page is displayed correctly."""
        response = client.get(reverse("polls:index"))
        assert response.status_code == 200
        assert "No polls are available." in str(response.render().content)
        assert len(response.context["latest_question_list"]) == 0

    @freeze_time("2017-01-01")
    def test_past_question(self, client):
        """Ensure normal questions show."""
        question = create_question(question_text="Past question", days=-30)
        response = client.get(reverse("polls:index"))
        assert list(response.context["latest_question_list"]) == [question]

    @freeze_time("2017-01-01")
    def test_future_question(self, client):
        """Ensure future questions are hidden from the index."""
        create_question(question_text="Future question", days=30)
        response = client.get(reverse("polls:index"))
        assert "No polls are available." in str(response.render().content)
        assert len(response.context["latest_question_list"]) == 0


class TestQuestionDetailView:

    @freeze_time("2017-01-01")
    def test_future_question(self, client):
        """Ensure future questions are hidden."""
        future_question = create_question(question_text="Future question",
                                          days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = client.get(url)
        assert response.status_code == 404

    @freeze_time("2017-01-01")
    def test_past_question(self, client):
        """Ensure questions are displayed."""
        past_question = create_question(question_text="Past question", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = client.get(url)
        assert past_question.question_text in str(response.render().content)
