from django.contrib import admin
from news.models import News
from sell.models import Reviews, Coaches
from users.models import UserProduct, Support, User

admin.site.register(News)
admin.site.register(Support)
admin.site.register(Reviews)
admin.site.register(UserProduct)
admin.site.register(Coaches)
admin.site.register(User)