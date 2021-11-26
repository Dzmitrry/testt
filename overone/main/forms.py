from .models import Feedback
from django import forms

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']