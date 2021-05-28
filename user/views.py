from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

# Create your views here.

# Register API


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "token": AuthToken.objects.create(user)[1]
        })


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
