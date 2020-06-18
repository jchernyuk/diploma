from django import forms

from learning.models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
