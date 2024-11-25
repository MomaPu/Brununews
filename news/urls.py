from django.urls import path
from news.views import index,sell,python_courses
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [path('index/', index),
               path('courses/',sell),
               path('courses/py_course', python_courses)
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

