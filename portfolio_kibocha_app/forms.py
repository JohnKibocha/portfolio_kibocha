from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['profile_photo', 'name', 'company_name', 'company_position', 'comment']
