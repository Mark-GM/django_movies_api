# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "username", "mobile_number", "password", "password_confirm")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):

        if self.validated_data.get("password") != self.validated_data.get(
            "password_confirm"
        ):
            raise serializers.ValidationError({"password": "Password doesn't match"})

        user = User(
            email=self.validated_data.get("email"),
            username=self.validated_data.get("username"),
            mobile_number=self.validated_data.get("mobile_number"),
        )

        user.set_password(self.validated_data.get("password"))
        user.save()
        return user
