
from django.conf.urls import url, include
# from django.contrib import admin
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teachers', views.TeacherViewSet)

urlpatterns = [
    url(r'^', include(router.urls))

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^admin/', admin.site.urls),
]
