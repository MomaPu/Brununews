from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from sell.forms import CourseFilterForm
from sell.models import Product, Reviews
from sell.services import get_coaches, CourseFilter, create_review

COURSE_CHOICES = {
    '1': 'Маркетинг',
    '2': 'Программирование',
    '3': '3D-Дизайн',
}

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
    return render(request, 'sell/Python_courses.html', context)


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


def coach_info(request):

    coaches = get_coaches()

    return render(request,'coaches/coach_info.html', {'coach': coaches})

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