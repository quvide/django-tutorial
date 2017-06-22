from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from polls.api import polls

router = routers.DefaultRouter()
router.register(r"question", polls.QuestionViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r"^api-swagger/", get_swagger_view(title="Polls API")),
    url(r"^polls/", include("polls.urls")),
]

urlpatterns += i18n_patterns(url(r"^admin/", include(admin.site.urls)))
