from sell.models import Product, Reviews, Category
from news.models import News
from django.shortcuts import get_object_or_404
from sell.models import Category

COURSE_CHOICES = [('', 'Все категории')]
for category in Category.objects.all():
    COURSE_CHOICES.append((category.name, category.name))


def get_courses_by_category(category_id):
    if not category_id:
        return Product.objects.all()
    try:
        category = Category.objects.get(id=int(category_id))
        return Product.objects.filter(category=category)
    except Category.DoesNotExist:
        return Product.objects.none()


def get_new_news():

    return list(News.objects.all())
def create_review(course_id, review_text, user):

    course = get_object_or_404(Product.objects.select_for_update(), id=course_id)
    return Reviews.objects.create(article=course, text=review_text, user=user)
def get_courses():

    return Product.objects.all()
def get_reviews_list():

    return Reviews.objects.select_related('article', 'user').all()

