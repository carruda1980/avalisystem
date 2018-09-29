from rest_framework import serializers
from .models import Produto

from django.utils.text import slugify


class ProdutoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    produto = serializers.CharField(required=True, max_length=255)
    slug = serializers.CharField(required=False, max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Produto` instance, given the validated data.
        """
        validated_data.update({'slug': slugify(validated_data['produto'])})
        return Produto.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.produto = validated_data.get('produto', instance.produto)
        instance.slug = slugify(validated_data['produto'])
        return instance

class ProdutoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'produto',)