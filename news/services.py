from sell.models import Product
from news.models import News
def get_py_courses():
    return list(Product.objects.filter(name__icontains="Python"))
def get_3d_courses():
    return list(Product.objects.filter(name="3D-Дизайн"))
def get_marketing_courses():
    return list(Product.objects.filter(name="Маркетинг"))

def get_new_news():
    return list(News.objects.all()[:3])
def get_all_news():
    return list(News.objects.all()[3:])