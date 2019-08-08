from django.conf.urls import url
from dailyfresh.views import register
urlpatterns=[
    url('register',register),
]