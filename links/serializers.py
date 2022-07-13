from rest_framework import serializers
from .models import Link
from django.contrib.auth.models import User


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'name', 'url']


class UserSerializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
