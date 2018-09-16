# from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Produto
from api.serializers import ProdutoSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics

from rest_framework.views import APIView


def index(request):
    return HttpResponse('Bora programar api!!!')

def produto_list(request):
    """
    Lista todos os produtos.
    """
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProdutoCreate(APIView):
    """
    Cria um novo produto.
    """
    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdutoDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    """
    Detalhes do produto.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProdutoDelete(mixins.DestroyModelMixin, 
                    generics.GenericAPIView):
    """
    Deleta produto.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)