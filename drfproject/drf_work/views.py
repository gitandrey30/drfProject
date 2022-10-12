from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer


@api_view(['GET', 'POST'])
def get_product(request):
    if request.method == 'POST':
        products = request.data
        print(products)
        products_serialized = ProductPOSTSerializer(data=products)
        if products_serialized.is_valid(raise_exception=True):
            print(products_serialized.validated_data)
            # products_serialized.create(**validated_data)
        else:
            print(products_serialized.errors)

        return Response('ok')

    product = Product.objects.all()
    products_serialized = ProductSerializer(product, many=True)

    return Response(products_serialized.data)

@api_view(['GET'])
def get_category(request):
    categories = Category.objectts.all()
    category_serializer = CategorySerializer(categories , many=True)

    return Response(CategorySerializer.data)