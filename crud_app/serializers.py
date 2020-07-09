from rest_framework import serializers
from .models import userProfile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])

        user.save()
        Token.objects.create(user=user)
        return user
