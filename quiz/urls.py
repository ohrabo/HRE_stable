from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.qpage, name='quiz_home'),
]