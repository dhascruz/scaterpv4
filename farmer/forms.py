from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, FarmerDetail

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')

class FarmerDetailForm(forms.ModelForm):
    class Meta:
        model = FarmerDetail
        fields = ('phone','pincode','village','taluk','district','state','country')
