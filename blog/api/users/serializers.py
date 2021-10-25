from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(min_length=100)