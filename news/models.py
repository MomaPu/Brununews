from django.db import models

class News(models.Model):
    title = models.CharField("Название",max_length=64, unique=True)
    text = models.TextField("Текст новости")
    image = models.ImageField("Изображение", upload_to='products/images/', null=True, blank=True)
    def __str__(self):
        return self.title

