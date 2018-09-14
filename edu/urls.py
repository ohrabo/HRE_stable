from django.urls import path

from edu.views import CourseListView
from . import views

urlpatterns = [
path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
path('create/', views.CourseCreateView.as_view(), name='course_create'),
path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
path('<pk>/module/',views.CourseModuleUpdateView.as_view(),name='course_module_update'),
path('module/<module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='module_content_create'),
path('module/<module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(), name='module_content_update'),
path('content/<id>/delete/',views.ContentDeleteView.as_view(),name='module_content_delete'),
path('module/<module_id>/',views.ModuleContentListView.as_view(),name='module_content_list'),
path('learn/', CourseListView.as_view(), name='course_list'),
path('learn/subject/<subject>/', views.CourseListView.as_view(), name='course_list_subject'),
path('learn/<slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]