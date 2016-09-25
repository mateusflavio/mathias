from django.conf.urls import url

from mathias.user.views import UserList
from mathias.valeu.views import ValeuList, ValeuDetail

urlpatterns = [
    url(r'^$', UserList.as_view()),
]
