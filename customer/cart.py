from decimal import Decimal
from django.conf import settings
from applications.models import products


class Cart_insert(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, Product, quantity=1, update_quantity=False):
        product_id = str(Product.products_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'id':Product.products_id,'quantity': 0, 'price': str(Product.products_price) ,'name' :Product.products_name ,'image':Product.products_image}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self,Product):
        product_ids = str(Product.products_id)
        if product_ids in self.cart:
            del self.cart[product_ids]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        productss = products.objects.filter(products_id__in=product_ids)
        for product in productss:
            self.cart[str(products.products_id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

