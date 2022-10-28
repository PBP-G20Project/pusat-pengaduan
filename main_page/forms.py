
from django import forms

from .models import *

class PostForms(forms.ModelForm):
    # comment= forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 15em;'}))

    class Meta:
        model = Comments
        fields = ['comment']