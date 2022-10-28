
from django.forms import ModelForm
from django import forms
from .models import *

class FormReviews(ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'comment']

        widgets = {
            'rating' : forms.NumberInput({'class':'form-control'}),   
            'comment' : forms.Textarea({'class':'form-control'}),    
        }

# class PostForms(forms.ModelForm):
#     # comment= forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 15em;'}))

#     class Meta:
#         model = Comments
#         fields = ['comment']