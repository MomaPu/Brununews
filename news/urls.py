from django.urls import path
from news.views import index,sell,python_courses
urlpatterns = [path('index/', index),
               path('courses/',sell),
               path('courses/py_course', python_courses)
    ]