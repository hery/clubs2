
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Teacher

from api.serializers import TeacherSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format='json'):
        user = self.get_object(username)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)


class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
