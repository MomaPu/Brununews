# coding: utf-8
update.Product
products = Product.objects.all()
from sell.models import Product
products = Product.objects.all()
products[0].stock
products[0].stock.set(0)
UPDATE products SET stock = 0 WHERE id=0
UPDATE Product SET stock = 0 WHERE id=0
UPDATE product SET stock = 0 WHERE id=0
UPDATE sell_product SET stock = 0 WHERE id=0
products[0].stock = 0
Product.objects.all()[0].stock = 0
