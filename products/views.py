from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework import status
from products.history import History
from products.models import Product
from products.serializers import ProductValidateSerializer


@require_POST
def history_add(request, product_id):
    post = History(request)
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductValidateSerializer(post, many=False)
    if not serializer.is_valid():
        return Response(data={'errors': serializer.errors})
    else:
        post.add(product=product)
    return Response('сохранился')


def history_remove(request, product_id):
    post = History(request)
    product = get_object_or_404(Product, id=product_id)
    post.remove(product)
    return Response('Удалено')


def history_clear(request):
    post = History(request)
    post.clear()
    return Response('ВСЁ Удалено ')


def history_detail(request):
    post = History(request)
    for item in post:
        post = item
        serializer = ProductValidateSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer


@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        posts = Product.objects.all()
        serializer = ProductValidateSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('text')
        price = serializer.validated_data.get('price')
        quantity = serializer.validated_data.get('quantity')
        size = serializer.validated_data.get('size')
        color = serializer.validated_data.get('color')
        post = Product.objects.create(title=title, text=text, price=price, quantity=quantity)
        post.tags.set(post)
        post.tags.set(color)
        post.save()
        return Response(data={'post': ProductValidateSerializer(post).data})


@api_view(['DELETE'])
def product_delete_view(request, **kwargs):
    try:
        post = Product.objects.get(id=kwargs['id'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'ERROR'})
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
