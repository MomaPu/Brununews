from django.urls import path
from news.views import get_news, news_detail
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('index/', get_news, name='get_news'),
    path('news/<int:id>/', news_detail, name='news_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
