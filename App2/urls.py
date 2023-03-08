from App1.views import *
from django.urls import path

from App2.views import raina
app_name='nothing'
urlpatterns = [
    path('raina/',raina,name='raina'),
]