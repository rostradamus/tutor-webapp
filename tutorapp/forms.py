from django import forms
from django.utils import timezone
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('course_name', 'course_number', 'start_at', 'end_at', 'comment')
        widgets = {
            # TODO: Hope these in html ui to be date/time picker (maybe using angular.js/JQuery)
            'start_at': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'end_at': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }


class SearchForm(forms.ModelForm):
    # TODO: Search form must be specified
    class Meta:
        model = Post
        fields = '__all__'

