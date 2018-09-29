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

class ProdutoList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProdutoCreate(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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

class ProdutoUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    Update produto.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def update(self, *args, **kwargs):
        produto = self.get_object()
        serializer = ProdutoSerializer(produto, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)