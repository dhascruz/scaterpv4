from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')

class FarmerDetailForm(forms.ModelForm):
    class Meta:
        model = FarmerDetail
        fields = ('phone','pincode','village','taluk','district','state','country')



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']


class CustomLoginForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


# class AppointmentForm(forms.ModelForm):


#     # doctor = forms.ChoiceField(
        
#     #     widget=forms.Select(attrs={'class': 'form-control'})
#     # )
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     mobile_number = forms.CharField(
#         max_length=15,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     patient_id = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
   
#     appointment_date = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'})
#     )

#     email = forms.CharField(
#         max_length=50,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
        
#     appointment_fees = forms.DecimalField(
#         initial=150.00,
#         widget=forms.NumberInput(attrs={'readonly': 'readonly'})
#     )        

#     # patient_address = forms.CharField(
#     #     max_length=200,
#     #     widget=forms.TextInput(attrs={'class': 'form-control'})
#     # )
#     # patient_fees = forms.CharField(
#     #     max_length=10,
#     #     widget=forms.TextInput(attrs={'class': 'form-control'})
#     # )
#     class Meta:
#         model = Appointment
        
#         fields = ['name', 'mobile_number', 'patient_id', 'appointment_date', 'slot', 'email', 'address',  'appointment_fees']
#     widgets = {
#             'appointment_date': forms.DateInput(attrs={'type': 'date'}),
#        }


        

class AgriProductForm(forms.ModelForm):


    crop_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


    actual_production = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    project_production = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    projection_timeline = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    cultivation_land_value = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
     
    cost_per_unit = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    project_cost_per_unit = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )



    
    class Meta:
        model = AgriProduct
        fields = [
            'category',
            'crop_name',
            'actual_production',
            'project_production',
            'projection_timeline',
            'cultivation_land_value',
            'cost_per_unit',
            'project_cost_per_unit',
            'image',
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'description']


     
                  



class AgriAssetForm(forms.ModelForm):

    land_owner = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    land_location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


    google_map_location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    width = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    length = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    size = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    

    class Meta:
        model = AgriAsset
        fields = ['land_owner', 'land_location', 'google_map_location', 'width', 'length', 'size', 'cultivation_method','owner_type']


class ContactForm(forms.ModelForm):


    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    phone = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    referral = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )



    class Meta:
        model = Contact
        fields = ['user','name', 'phone', 'email', 'referral' ]