
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


urlpatterns = format_suffix_patterns([
    url(r'^api/$', views.api_root),

    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^api/teachers/$', views.TeacherList.as_view(), name='teacher-list'),
    url(r'^api/teachers/(?P<pk>[0-9]+)/$', views.TeacherDetail.as_view(), name='teacher-detail'),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^admin/', admin.site.urls),
])
