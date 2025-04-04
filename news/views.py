from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib import messages
from news.models import Support, News
from sell.models import Product, Reviews
from news.services import CourseFilter, get_new_news, create_review
from news.forms import CourseFilterForm
import logging

logger = logging.getLogger(__name__)

COURSE_CHOICES = {
    '1': 'Маркетинг',
    '2': 'Программирование',
    '3': '3D-Дизайн',
}
def index(request):

    print("Courses fetched:")
    return render(request, 'news/index.html')


def get_all_courses(request):

    all_courses = list(COURSE_CHOICES.keys())

    print("All Courses fetched:", all_courses)

    py_courses = [course for course in all_courses if "programming" in course.name]
    threed_courses = [course for course in all_courses if "three_d" in course.name]
    marketing_courses = [course for course in all_courses if "marketing" in course.name]

    print("Python Courses:", py_courses)
    print("3D Courses:", threed_courses)
    print("Marketing Courses:", marketing_courses)

    context = {
        'py_courses': [course for course in all_courses if "Python" in course.name],
        'threed_courses': [course for course in all_courses if "3D-Дизайн" in course.name],
        'marketing_courses': [course for course in all_courses if "Маркетинг" in course.name],
    }
    return render(request, 'news/Python_courses.html', context)


def find_courses(request):
    form = CourseFilterForm(request.GET)
    filtered_courses = Product.objects.all()

    if form.is_valid():
        course_filter = CourseFilter(**form.cleaned_data)
        filtered_courses = course_filter.find()
    else:
        print("Form errors:", form.errors)

    context = {
        'py_courses': [course for course in filtered_courses if "Python" in course.name],
        'threed_courses': [course for course in filtered_courses if "3D-Дизайн" in course.name],
        'marketing_courses': [course for course in filtered_courses if "Маркетинг" in course.name],
        'form': form
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
    return render(request, 'news/index.html', context)


def support_view(request):

    if request.method == 'POST':
        mail = request.POST.get('recipient-name')
        text = request.POST.get('message-text')

        Support.objects.create(mail=mail, text=text)

    return render(request, 'news/support.html')


def reviews(request):

    if request.method == 'POST':

        return handle_post_review(request)

    courses = Product.objects.all()
    reviews_list = Reviews.objects.all().select_related('product', 'user')

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
        with transaction.atomic():
            create_review(course_id, review_text, user)
        messages.success(request, 'Отзыв отправлен!')

    return redirect('reviews')

def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news/news_title.html', {'news': news_item})

