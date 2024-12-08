from django.shortcuts import render
from news.services import get_py_courses, get_3d_courses,get_marketing_courses
def index(request):
    return render(request, 'news/index.html')


def get_all_courses(request):
    py_courses = get_py_courses
    threed_courses = get_3d_courses()
    marketing_courses = get_marketing_courses()
    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }
    return render(request,'news/Python_courses.html', context)
def sell(request):
    py_courses = get_py_courses
    threed_courses = get_3d_courses()
    marketing_courses = get_marketing_courses()
    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }
    return render(request, 'sell/courses.html', context)

