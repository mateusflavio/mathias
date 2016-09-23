from django.conf.urls import url, include

from mathias.healthcheck.views import HealthcheckView

urlpatterns = [
    url(r'^$', HealthcheckView.as_view()),
]
