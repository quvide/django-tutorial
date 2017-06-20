from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from polls.api import polls

router = routers.DefaultRouter()
router.register(r"question", polls.QuestionViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-swagger/", get_swagger_view(title="Polls API")),
    url(r"^polls/", include("polls.urls")),
    url(r'^admin/', admin.site.urls)
]
