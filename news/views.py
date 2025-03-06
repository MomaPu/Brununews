from django.shortcuts import render, redirect
from news.services import get_py_courses, get_3d_courses,get_marketing_courses, get_new_news, create_review, get_courses, get_reviews_list
from django.core.paginator import Paginator
from news.models import Support
from sell.models import Product, Reviews
from django.contrib import messages

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
    print("Courses fetched:", py_courses, threed_courses, marketing_courses)  
    context = {
        'py_courses': py_courses,
        'threed_courses': threed_courses,
        'marketing_courses': marketing_courses
    }
    return render(request, 'sell/courses.html', context)


def get_news(request):
    new_news = get_new_news()[:3]
    all_news = get_new_news()[3:]
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
def support_view(request):
    if request.method == 'POST':
        mail = request.POST.get('recipient-name')
        text = request.POST.get('message-text')

        Support.objects.create(mail=mail, text=text)

    return render(request, 'news/support.html')


def reviews(request):
    if request.method == 'POST':
        return handle_post_review(request)

    courses = get_courses()
    reviews_list = get_reviews_list()  

    return render(request, 'news/reviews.html', {
        'courses': courses,
        'reviews': reviews_list,
        'success_message': ''
    })


def handle_post_review(request):
    course_id = request.POST.get('course')
    review_text = request.POST.get('review')
    user = request.user if request.user.is_authenticated else None

    if course_id and review_text:
        create_review(course_id, review_text, user)
        messages.success(request, 'Отзыв отправлен!')

    return redirect('reviews')