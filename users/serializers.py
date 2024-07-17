from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[validate_password])
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "password2"]
        read_only_fields = ["id"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({
                "detail": "Password fields did not match"
            })

        return data

    def create(self, validated_data):
        validated_data.pop("password2")

        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user