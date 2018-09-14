from django.urls import path

from . import views

app_name='library'

urlpatterns = [
# text views
path('', views.text_list, name='text_list'),
path('tag/<tag_slug>/', views.text_list, name='text_list_by_tag'),
path('<year>/<month>/<day>/<text>/', views.text_detail, name='text_detail'),
path('<text_id>/share/', views.text_share, name='text_share'),
]