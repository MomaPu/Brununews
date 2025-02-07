from django.contrib import admin
from news.models import News,support
from sell.models import Reviews

admin.site.register(News)
admin.site.register(support)
admin.site.register(Reviews)
