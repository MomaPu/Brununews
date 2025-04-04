from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from sell.models import Product

class User(AbstractUser):
    pass

class UserProduct(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='customers', on_delete=models.CASCADE)
    purchase_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} purchased {self.product.name} on {self.purchase_at}"



