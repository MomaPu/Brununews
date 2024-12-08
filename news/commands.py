from django.core.management.base import BaseCommand
from faker import Faker
from news.factories import BookFactory

class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми данными'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            BookFactory.create()
        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена!'))
