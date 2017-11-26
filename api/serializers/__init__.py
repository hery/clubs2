
from django.contrib.auth.models import User
from api.models import Teacher
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = (
            'url',
            'user',
            'city',
            'style',
            'ratings',
            'description',
            'featured'
        )
        depth = 1