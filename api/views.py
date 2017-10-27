
from django.contrib.auth.models import User

from rest_framework import viewsets

from api.models import Teacher
from api.serializers import TeacherSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer	


class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
