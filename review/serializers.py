from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class ReviewCreateSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(min_value=1, max_value=5)
    review = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = (
            'score',
            'review',
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    score = serializers.IntegerField(min_value=1, max_value=5)
    review = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = (
            'user',
            'score',
            'review',
        )
