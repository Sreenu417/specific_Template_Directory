from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('third/',third,name='third'),
    path('four/',four,name='four'),
]