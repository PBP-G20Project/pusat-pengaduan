from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django import forms 
from django.contrib.auth.forms import UserCreationForm 
 
User = get_user_model()
 
class SignUpForm(UserCreationForm): 
    class Meta: 
        model = User
        fields = ('email', 'nama', 'nik', 'password1', 'password2', )