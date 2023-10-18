from request.models import Request
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default = 0)
    class Meta:
        model = Request
        fields = ['path', 'quantity']