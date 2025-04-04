from django.urls import path
from news.views import get_news, find_courses, get_all_courses, support_view, reviews, news_detail
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('index/', get_news, name='get_news'),
    path('courses/', find_courses, name='find_courses'),
    path('courses/py_course/', get_all_courses, name='get_all_courses'),
    path('support/', support_view, name='support_view'),
    path('reviews/', reviews, name='reviews'),
    path('accounts/logout/', LogoutView.as_view(next_page='get_news'), name='logout'),
path('news/<int:id>/', news_detail, name='news_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
