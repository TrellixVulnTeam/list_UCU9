from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^person/$',person_views),
]