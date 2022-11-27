from rest_framework import serializers

from .models import Product


class ProdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    product_set = serializers.RelatedField(queryset=Product.objects.all(), many=True)


class ProductPOSTSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = serializers.IntegerField()