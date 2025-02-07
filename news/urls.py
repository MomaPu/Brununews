from django.urls import path
from news.views import get_news,sell, get_all_courses, support_view, reviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [path('index/', get_news,),
               path('courses/',sell),
               path('courses/py_course', get_all_courses),
               path('support/', support_view, name='support_view'),
               path('reviews/', reviews, name='reviews')
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

