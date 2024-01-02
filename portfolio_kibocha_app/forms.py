from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['profile_photo', 'name', 'place_of_work', 'job_description', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'John Doe'}),
            'place_of_work': forms.TextInput(attrs={'placeholder': 'Google Inc.'}),
            'job_description': forms.TextInput(attrs={'placeholder': 'Software Engineer'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Enter your comment'}),
            'profile_photo': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
        labels = {
            'name': 'Name (Required)',
            'place_of_work': 'Organization or Business Name',
            'job_description': 'Occupation or Profession (Required)',
            'comment': 'Comment (Required)',
            'profile_photo': 'Upload Profile Photo',
        }
