from datetime import date
from django.test import TestCase
from news.factories import ProductFactory, CategoryFactory, AuthorFactory, BookFactory
from sell.models import Product, Category
from news.services import create_review, get_courses, get_reviews_list, get_courses_by_category
from django.contrib.auth import get_user_model



class TestCourses(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name="Тестовая категория")

        self.python_course = Product.objects.create(name="Курс по Python", price=100.00, text="Введение в Python",
                                                    category=self.category, stock=10)
        self.advanced_python_course = Product.objects.create(name="Продвинутый курс по Python", price=150.00,
                                                             text="Углубленное изучение Python", category=self.category,
                                                             stock=10)
        self.java_course = Product.objects.create(name="Курс по Java", price=120.00, text="Введение в Java",
                                                  category=self.category, stock=10)

    def test_get_courses_by_valid_categories(self):
        courses = get_courses_by_category(['Python', '3D-Дизайн'])
        self.assertEqual(len(courses), 2)

    def test_get_courses_by_invalid_category(self):
        with self.assertRaises(ValueError):
            get_courses_by_category(['Неподдерживаемая категория'])


    def test_create_review(self):
        review_text = "Отличный курс!"
        review = create_review(course_id=self.python_course.id, review_text=review_text, user=self.user)
        self.assertEqual(review.article, self.python_course)
        self.assertEqual(review.text, review_text)
        self.assertEqual(review.user, self.user)

    def test_get_courses(self):
        result = get_courses()
        self.assertEqual(list(result), [self.python_course, self.advanced_python_course, self.java_course])

    def test_get_reviews_list(self):
        create_review(course_id=self.python_course.id, review_text="Отличный курс!", user=self.user)
        reviews = get_reviews_list()
        self.assertEqual(reviews.count(), 1)
        self.assertEqual(reviews.first().text, "Отличный курс!")


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
