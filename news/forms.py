from django import forms
from sell.models import Reviews, Category

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text',)


class CourseFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, label='Минимальная цена')
    max_price = forms.DecimalField(required=False, label='Максимальная цена')
    category = forms.ChoiceField(choices=[], required=False, label='Выберите категорию')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(category.id, category.name) for category in Category.objects.all()]
