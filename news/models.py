from django.db import models

class Article(models.Model):
    """
    Статья на сайте
    """
    class Status(models.TextChoices):
        DRAFT = "draft", "На модерации"
        PUBLISH = "publish", "Готово к публикации"
        INACTIVE = "inactive", "Неактивное"

    author = models.ForeignKey('users.User', related_name='Articles',on_delete=models.SET_NULL,null=True, default=None)

    title = models.CharField("Заголовок",max_length=64, unique=True)
    description = models.CharField("Заголовок новости", max_length=200)
    text = models.TextField("Текст новости")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    pub_date = models.DateTimeField("Дата публикации")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
