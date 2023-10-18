from request.models import Request
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default = 0)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['path', 'quantity', 'url']

    def get_url(self, obj):
        product = obj['path'].split('/')[-1] if obj['path'] else None

        if product is None:
            return product
        
        return f'https://pechinchou.com.br/oferta/{product}/'