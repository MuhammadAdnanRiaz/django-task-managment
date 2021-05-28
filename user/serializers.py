from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from knox.models import AuthToken
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


# Register User
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user
