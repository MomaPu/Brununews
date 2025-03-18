from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from news.models import Support
from sell.models import Product, Category
from news.services import get_courses_by_category, get_new_news, create_review, get_reviews_list
from news.forms import CourseFilterForm
import logging

logger = logging.getLogger(__name__)

COURSE_CHOICES = [('', 'Все категории')]
for category in Category.objects.all():
    COURSE_CHOICES.append((category.name, category.name))


def index(request):
    print("Courses fetched:")
    return render(request, 'news/index.html')


def get_all_courses(request):
    all_courses = get_courses_by_category(list(COURSE_CHOICES.keys()))

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


def sell(request):
    print("COURSE_CHOICES:", COURSE_CHOICES)
    form = CourseFilterForm(request.GET)

    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        category = form.cleaned_data.get('category')

        print("Selected category:", category)
        print("Max", max_price)

        filtered_courses = get_courses_by_category(category)

        # Логика фильтрации по цене
        if min_price is not None:
            filtered_courses = filtered_courses.filter(price__gte=min_price)
        if max_price is not None:
            filtered_courses = filtered_courses.filter(price__lte=max_price)

    else:
        filtered_courses = Product.objects.all()
        print("Form errors:", form.errors)
        #
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

    courses = get_courses_by_category(list(COURSE_CHOICES.values()))  # Подобрать курсы здесь
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
