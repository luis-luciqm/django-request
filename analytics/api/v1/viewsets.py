from rest_framework.views import APIView, Response
from analytics.api.v1.serializers import RequestSerializer

from request.models import Request
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count

class RequestPechinchouSaveViewSet(APIView):

    def post(self, request, *args, **kwargs):
        try:
            object = request.data
            data = Request(**object)
            data.save()

            return Response({'message': 'Salvo com sucesso!'})
        except Exception as e:
            return Response({'error': f'Ocorreu um erro ao salvar: {e}'})
        
class ViewAndAgroupRoutesByDetailOfProductMostAccessedInAPPLastMinute(APIView):
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        # TransactionAmazon.objects.filter(data__date = endDate).values('nome').annotate(data = Max('data'), categoria = Max('categoria'), dispositivo = Max('dispositivo'), price = Max('price'), qtd_pedidos = Max('qtd_pedidos'), quantity = Count('nome')).order_by('-quantity')

        # preciso pegar todas as requests do ultimo minuto
        requests = Request.objects \
            .filter(path__icontains = '/api/v2/produto/novo_detalhe_produto/'
            , time__gte = (timezone.now() - timedelta(minutes = 1))) \
            .values('path') \
            .annotate(quantity = Count('path')) \
            .order_by('-quantity')[:30]

        serializer = self.serializer_class(requests, many = True)
        data = serializer.data

        return Response(data)
