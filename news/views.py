from django.shortcuts import render
from news.services import get_py_courses, get_3d_courses,get_marketing_courses, get_new_news,get_all_news
from django.core.paginator import Paginator

def index(request):
    print("Courses fetched:")
    return render(request, 'news/index.html')


def get_all_courses(request):
    py_courses = get_py_courses()
    threed_courses = get_3d_courses()
    marketing_courses = get_marketing_courses()
    print("Python Courses:", py_courses)
    print("3D Courses:", threed_courses)
    print("Marketing Courses:", marketing_courses)
    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }
    return render(request,'news/Python_courses.html', context)
def sell(request):
    py_courses = get_py_courses()
    threed_courses = get_3d_courses()
    marketing_courses = get_marketing_courses()
    print("Courses fetched:", py_courses, threed_courses, marketing_courses)  # Отладочный вывод
    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }
    return render(request, 'sell/courses.html', context)


def get_news(request):
    new_news = get_new_news()
    all_news = get_all_news()
    paginator = Paginator(all_news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print("Новые новости:", new_news)
    print("Все новости:", all_news)
    context = {
        'new_news': new_news,
        'page_obj': page_obj
    }
    return render(request,'news/index.html',context)
