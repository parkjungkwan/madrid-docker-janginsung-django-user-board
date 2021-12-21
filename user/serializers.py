from rest_framework import serializers
# pip install Django django-rest-framework
from .models import User as user


class UserSerializer(serializers.Serializer):
    user_email = serializers.CharField()
    password = serializers.CharField()
    user_name = serializers.CharField()
    phone = serializers.CharField()
    birth = serializers.CharField()
    address = serializers.CharField()
    job = serializers.CharField()
    user_interests = serializers.CharField()

    class Meta:
        model = user
        fields = '__all__'

    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user.objects.filter(pk=instance.id).update(**validated_data)