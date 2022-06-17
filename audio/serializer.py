from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from audio.models import *


class AudioKnigaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AudioKniga
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class WishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'