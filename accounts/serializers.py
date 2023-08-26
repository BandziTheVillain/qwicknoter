from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSignupSerializer(UserCreateSerializer):
    tokens = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("username", "email", "password", "tokens",)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
        
    def get_tokens(self, obj):
        refresh = RefreshToken.for_user(obj)
        access = refresh.access_token
        return {
            "access": str(access),
            "refresh": str(refresh)
        }