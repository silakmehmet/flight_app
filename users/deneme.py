from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "password2")
        read_only_fields = ("id",)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({
                "detail": "Password fields didn't match.",
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.get("password")
        user_instance = User.objects.create(**validated_data)
        user_instance.set_password(password)
        user_instance.save()
        return user_instance
