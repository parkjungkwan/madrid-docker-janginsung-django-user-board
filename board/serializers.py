from rest_framework import serializers
# pip install Django django-rest-framework
from .models import Board as board

#  use_in_migrations = True
#     title = models.TextField(max_length=100)
#     body = models.TextField()
#     comment = models.TextField()
#     writen = models.ForeignKey(User, on_delete=models.CASCADE)
#     create_at = models.DateTimeField()
#     update_at = models.DateTimeField()


class BoardSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    comment = serializers.CharField()
    writen = serializers.CharField()
    create_at = serializers.CharField()
    update_at = serializers.CharField()

    class Meta:
        model = board
        fields = '__all__'

    def create(self, validated_data):
        return board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        board.objects.filter(pk=instance.id).update(**validated_data)