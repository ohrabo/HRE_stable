
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from edu.views import CourseListView

urlpatterns = [
# path('userprofile/login/', auth_views.login, name='login'),
#     path('userprofile/logout/', auth_views.logout, name='logout'),
# path('userprofile/logout-then-login/',  auth_views.logout_then_login, name='logout_then_login'),

    path('edu/login/', auth_views.login, name='login'),
    path('edu/logout/', auth_views.logout, name='logout'),
    path('edu/logout-then-login/',  auth_views.logout_then_login, name='logout_then_login'),
    path('library/', include('library.urls'), name='library'),
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
    path('quiz/', include ('quiz.urls')),
    path('edu/', include('edu.urls')),
    path('learn/', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
