from django.shortcuts import render
from sell.models import Product

def index(request):
    return render(request, 'news/index.html')


def python_courses(request):
    py_courses = Product.objects.filter(name="Программирование Python").first()
    threed_courses = Product.objects.filter(name="3D-Дизайн").first()
    marketing_courses = Product.objects.filter(name="Marketing").first()
    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }
    return render(request,'news/Python_courses.html', context)
def sell(request):
    products = Product.objects.all()

    py_courses = products[0] if products else None
    threed_courses = products[1] if len(products) > 1 else None
    marketing_courses = products[2] if len(products) > 2 else None

    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }

    return render(request, 'sell/courses.html', context)

