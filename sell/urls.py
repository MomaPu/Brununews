from django.urls import path, include
from sell.views import coach_info
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('coaches/', coach_info, name='coach_info')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
