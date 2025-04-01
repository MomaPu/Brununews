from django.db import models

class Category(models.Model):

    objects = None
    name = models.CharField("Наименование",max_length=100, unique=True)


class Product(models.Model):

    name = models.CharField("Название",max_length=64, unique=True)
    price = models.DecimalField("Стоимость", max_digits=12, decimal_places=2)
    text = models.TextField("Текст новости")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    image = models.ImageField("Изображение", upload_to='products/images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    product = models.ForeignKey('sell.Product', related_name='Отзыв', on_delete=models.CASCADE )
    text = models.TextField('Текст отзыва')
    user = models.ForeignKey('users.User', related_name='Отзыв', null = True, on_delete=models.SET_NULL)
    is_anon = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        if self.user is None:
            self.is_anon = True
        return super().save(*args, **kwargs)
    def __self__(self):
        username = self.user.username if self.user is not None else 'Анонимный пользователь'
        return f"{self.artice.title}/{self.user.username}"