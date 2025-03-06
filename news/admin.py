from django.contrib import admin
from news.models import News,Support
from sell.models import Reviews

admin.site.register(News)
admin.site.register(Support)
admin.site.register(Reviews)
