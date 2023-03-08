from rest_framework import serializers
from .models import *
from rest_framework.serializers import ValidationError
from product.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemValidateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1)

    def validate_product_id(self, product_id):
        product_exists = Product.objects.filter(id=product_id).exists()
        if product_exists:
            return product_id
        raise ValidationError('Given product does not exists')


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = 'id user items total_price'.split(' ')

    def get_items(self, cart):
        return cart.cart_items_list()

    def get_total_price(self, cart):
        return cart.total_price()