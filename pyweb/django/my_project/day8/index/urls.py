from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^remark/$', remark_views),
    url(r'^register/$',register_views),
    url(r'^model_form/$',model_form_views),
]