# Necessary imports
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .serializers import UserSerializer

# Get the custom user model
User = get_user_model()


# UserViewSet: View for retrieving, listing, and updating users
class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        # Filter users so that only the current user can access their own profile
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        # Custom action to get the profile of the current user
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# UserCreateViewSet: View for creating new users
class UserCreateViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# UserDeleteViewSet: View for deleting existing users
class UserDeleteViewSet(DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        # Customize the logic for deleting a user if necessary
        instance.delete()


# PasswordResetView: View for resetting the password
class PasswordResetView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["POST"])
    def reset_password(self, request):
        # Logic for sending a password reset email and generating a token
        # This is a basic example and should be customized for your application
        user = request.user
        user.password_reset_token = "generated_token"
        user.password_reset_expires = "expiration_date"
        user.save()
        return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
