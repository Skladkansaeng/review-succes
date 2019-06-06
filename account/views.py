from django.contrib.auth.models import User
from rest_framework import mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account.serializers import UserSerializer
from .permissions import IsStaffOrTargetUser


class UserView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    model = User

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = User.objects.create_user(self.request.data['username'], self.request.data['email'],
                                        self.request.data['password'])
        user.first_name = self.request.data['first_name']
        user.last_name = self.request.data['last_name']
        user.save()

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
