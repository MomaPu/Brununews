from sell.models import Product, Reviews
from news.models import News

def get_py_courses():
    return list(Product.objects.filter(name__icontains="Python"))
def get_3d_courses():
    return list(Product.objects.filter(name="3D-Дизайн"))
def get_marketing_courses():
    return list(Product.objects.filter(name="Маркетинг"))

def get_new_news():
    return list(News.objects.all())
def create_review(course_id, review_text, user):
    course = Product.objects.get(id=course_id)
    return Reviews.objects.create(article=course, text=review_text, user=user)
def get_courses():
    return Product.objects.all()
def get_reviews_list():
    return Reviews.objects.select_related('article', 'user').all()

