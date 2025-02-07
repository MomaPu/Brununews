from django import forms
from sell.models import reviews

class CommentForm(forms.Modelform)
    class Meta:
        model = reviews
        fields = ('text')