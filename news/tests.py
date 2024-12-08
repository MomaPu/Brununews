from datetime import date
from django.test import TestCase
from news.factories import ProductFactory, CategoryFactory, AuthorFactory, BookFactory
from sell.models import Product, Category


class TestCourses(TestCase):
    def test_create_product(self):
        category = Category.objects.create(name="Тестовая категория")
        product = Product.objects.create(
            name="Тестовый продукт",
            price=10.00,
            text="Текст тестового продукта",
            category=category,
            stock=5
        )
        self.assertEqual(product.name, "Тестовый продукт")
        self.assertEqual(product.price, 10.00)


class ProductTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory.create(name="Тестовая категория")

    def test_create_product_with_factory(self):
        product = ProductFactory.create(category=self.category)
        self.assertIsNotNone(product.id)
        self.assertEqual(product.category, self.category)
        self.assertGreaterEqual(product.price, 1)
        self.assertIsInstance(product.text, str)

    def test_product_stock(self):
        product = ProductFactory.create(category=self.category, stock=10)
        self.assertEqual(product.stock, 10)


class AuthorBookTests(TestCase):
    def test_create_author(self):
        author = AuthorFactory.create(name="Тестовый Автор")
        self.assertEqual(author.name, "Тестовый Автор")

    def test_create_book_with_authors(self):
        authors = [AuthorFactory.create() for _ in range(3)]
        book = BookFactory.create(title="Тестовая Книга", authors=authors)

        self.assertEqual(book.title, "Тестовая Книга")
        self.assertEqual(list(book.authors.all()), authors)

    def test_author_books_relationship(self):
        author = AuthorFactory.create(name="Автор")
        book1 = BookFactory.create(title="Первая Книга", published_date=date.today())
        book2 = BookFactory.create(title="Вторая Книга", published_date=date.today())


        author.books.set([book1, book2])

        self.assertEqual(author.books.count(), 2)
        self.assertIn(book1, author.books.all())
        self.assertIn(book2, author.books.all())
