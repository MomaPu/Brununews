from django.test import TestCase
from news.factories import ProductFactory, CategoryFactory
from sell.models import Product, Category
from sell.services import create_review, get_courses, get_reviews_list
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
