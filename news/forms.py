from django import forms
from sell.models import Reviews, Category
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text',)


class CourseFilterForm(forms.Form):
    min_price = forms.IntegerField(required=False, label='Минимальная цена')
    max_price = forms.IntegerField(required=False, label='Максимальная цена')
    category = forms.ChoiceField(choices=[('', 'Все категории')] + [(str(c.id), c.name) for c in Category.objects.all()],
                                   required=False, label='Категория')
    with_reviews_only = forms.BooleanField(required=False, label='Только с отзывами')

