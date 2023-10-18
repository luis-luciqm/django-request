from request.models import Request
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default = 0)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['url', 'quantity']

    def get_url(self, obj):
        print(obj['path'].split('/'))
        product = obj['path'].split('/')[-2] if obj['path'] else None

        if product is None:
            return product
        
        return f'https://local.pechinchou.com.br/oferta/{product}/'