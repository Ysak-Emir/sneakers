from django.conf import settings
from products.models import Product


class History(object):

    def __init__(self, request):
        self.session = request.session
        favorites = self.session.get(settings.HISTORY_SESSION_ID)
        if not favorites:
            favorites = self.session[settings.HISTORY_SESSION_ID] = {}
        self.favorites = favorites

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.favorites:
            self.favorites[product_id] = {'quantity': 0, 'price': str(product.price)}

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.favorites:
            del self.favorites[product_id]
            self.save()

    def clear(self):
        del self.session[settings.HISTORY_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.HISTORY_SESSION_ID] = self.favorites
        self.session.modified = True

    def __iter__(self):
        product_id = self.favorites.keys()
        products = Product.objects.filter(id__in=product_id)
        for product in products:
            self.favorites[str(product.id)]['product'] = product