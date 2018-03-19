from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^amadon/buy$', views.process),
    url(r'^checkout$', views.display),
]
