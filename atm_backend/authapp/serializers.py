# serializers.py in your application

from .models import CommonUser
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CommonUser
        fields = ["username", "password", "email"]

    def create(self, validated_data):
        user = CommonUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
