from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from polls.api import polls

router = routers.DefaultRouter()
router.register(r"question", polls.QuestionViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^polls/", include("polls.urls")),
    url(r'^admin/', admin.site.urls),
]
