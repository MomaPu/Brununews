from django.urls import path, include
from sell.views import coach_info, reviews, find_courses, get_all_courses
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('courses/', find_courses, name='find_courses'),
    path('courses/py_course/', get_all_courses, name='get_all_courses'),
    path('reviews/', reviews, name='reviews'),
    path('coaches/', coach_info, name='coach_info')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
