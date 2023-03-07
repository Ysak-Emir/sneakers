from django.db import models
from sneakersshop2 import settings
from users.models import User


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def cart_items_list(self):
        return [{ "id": item.id, "cart_id": item.cart_id, "product_id": item.flower_id, "quantity": item.quantity } for
                item in self.items.all()]

    def total_price(self):
        return sum([item.price() for item in self.items.all()])

    def __str__(self):
        return self.user.email + ' cart'


class CartItem(models.Model):
    cart = models.ManyToManyField(Cart, related_name='items')
    product = models.ManyToManyField(User)
    quantity = models.IntegerField(default=1)

    def price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.cart) + 'cart item'

    def add_quantity(self, amount):
        self.quantity += amount
        self.save()