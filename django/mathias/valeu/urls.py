from django.conf.urls import url

from mathias.valeu.views import ValeuList, ValeuDetail

urlpatterns = [
    url(r'^$', ValeuList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', ValeuDetail.as_view()),
]
