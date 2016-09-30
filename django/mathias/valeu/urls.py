from django.conf.urls import url

from mathias.valeu.views import ValeuList, ValeuDetail, ValeuLeaderBoard

urlpatterns = [
    url(r'^$', ValeuList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', ValeuDetail.as_view()),
    url(r'^leaderboard/$', ValeuLeaderBoard.as_view())
]
