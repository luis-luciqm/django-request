from rest_framework.views import APIView, Response, status
from analytics.api.v1.serializers import RequestSerializer
from django.core.cache import cache

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
        minutes = self.request.GET.get('minutes')

        if not minutes:
            return Response({'error': 'É necessário enviar o parametro "minutes"!'}, status = status.HTTP_400_BAD_REQUEST)

        res = cache.get(minutes)
        if res:
            return Response(res, status = status.HTTP_200_OK)
        
        # preciso pegar todas as requests do ultimo minuto
        requests = Request.objects \
            .filter(path__icontains = '/api/produto/adicionar_view_melhorada_v2/'
                , time__gte = (timezone.now() - timedelta(minutes = int(minutes)))) \
            .values('path') \
            .annotate(quantity = Count('path')) \
            .order_by('-quantity')[:30]

        serializer = self.serializer_class(requests, many = True)
        data = serializer.data

        cache.set(minutes, data, timeout = 30)
        return Response(data, status = status.HTTP_200_OK)
