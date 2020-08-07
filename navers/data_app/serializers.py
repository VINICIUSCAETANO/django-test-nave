from navers.data_app.models import User, Naver, Project
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    navers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password']

class NaverSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']