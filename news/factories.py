import factory
from factory.django import DjangoModelFactory
from faker import Faker
from sell.models import Product, Category
from news.models import Author, Book

fake = Faker()


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('sentence', nb_words=2)
    price = factory.Faker('random_number', digits=2)
    text = factory.Faker('paragraph')
    category = factory.SubFactory(CategoryFactory)
    stock = factory.Faker('random_int', min=0, max=100)


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    published_date = factory.Faker('date')

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:

            return

        if extracted:
            for author in extracted:
                self.authors.add(author)
        else:

            for _ in range(3):
                author = AuthorFactory.create()
                self.authors.add(author)