from sell.models import Product
def get_py_courses():
    py_courses = Product.objects.filter(name="Программирование Python").first()
def get_3d_courses():
    threed_courses = Product.objects.filter(name="3D-Дизайн").first()
def get_marketing_courses():
    marketing_courses = Product.objects.filter(name="Marketing").first()