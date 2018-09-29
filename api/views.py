# from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Produto, Voto
from api.serializers import ProdutoSerializer, VotoSerializer
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

class VotoList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VotoCreate(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VotoDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    """
    Detalhes do Voto.
    """
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class MediaVotos(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, *args, **kwargs):

        try:
            produto = self.get_object()
        except:
            return JsonResponse({
            'produto': 'Produto não exite'
        })
        try:
            votos = produto.voto.all().values_list("nota", flat=True)
            media = sum(votos)/len(votos)
        except ZeroDivisionError:
            return JsonResponse({
            'msg': 'Não existem votos para o produto informado'
        })
        
        return JsonResponse({
            'media': media
        })
        