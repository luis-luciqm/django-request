from rest_framework.views import APIView, Response

from request.models import Request

class RequestPechinchouSaveViewSet(APIView):

    def post(self, request, *args, **kwargs):
        try:
            object = request.data
            data = Request(**object)
            data.save()

            return Response({'message': 'Salvo com sucesso!'})
        except Exception as e:
            return Response({'error': f'Ocorreu um erro ao salvar: {e}'})