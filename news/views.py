from django.shortcuts import render, redirect
from news.services import get_py_courses, get_3d_courses,get_marketing_courses, get_new_news,get_all_news
from django.core.paginator import Paginator
from news.models import support
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
def support_view(request):
    if request.method == 'POST':
        mail = request.POST.get('recipient-name')
        text = request.POST.get('message-text')

        support.objects.create(mail=mail, text=text)

    return render(request, 'news/support.html')


def reviews(request):
    success_message = ''
    if request.method == 'POST':
        course_id = request.POST.get('course')
        review_text = request.POST.get('review')

        if course_id and review_text:
            course = Product.objects.get(id=course_id)
            user = request.user if request.user.is_authenticated else None

            Reviews.objects.create(article=course, text=review_text, user=user)

            success_message = 'Отзыв отправлен!'
            messages.success(request, success_message)

            return redirect('reviews')

    courses = Product.objects.all()
    reviews_list = Reviews.objects.select_related('article','user').all()

    return render(request, 'news/reviews.html', {
        'courses': courses,
        'reviews': reviews_list,
        'success_message': success_message
    })
