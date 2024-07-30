from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.hello2, name='hello2'),
]
