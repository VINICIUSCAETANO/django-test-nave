from navers.data_app.models import User, Naver, Project
from navers.data_app.serializers import UserSerializer, NaverSerializer, ProjectSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics


# users CRUD
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# navers CRUD
class NaverList(generics.ListAPIView):
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NaverDetail(generics.RetrieveAPIView):
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer
    permission_classes = [permissions.IsAuthenticated]


# projects CRUD
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]