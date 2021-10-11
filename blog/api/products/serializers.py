from rest_framework import serializers

from shop.models import STATUS_CHOICES

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    cost = serializers.IntegerField()
    description = serializers.CharField()
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
