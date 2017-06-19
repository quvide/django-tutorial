from rest_framework import serializers, viewsets, permissions

from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ("question_text", "pub_date",
                  "was_published_recently", "choices")


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
