from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *
class UserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label=" confirmpassword")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class RegForm(forms.ModelForm):
    class Meta:
        model = customeregister
        exclude = ('user',)
        fields = ('name', 'phone', 'address', 'email')

class SellForm(forms.ModelForm):
    class Meta:
        model = sellregister
        exclude = ('user',)
        fields = ('name', 'phone', 'address', 'email')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ('category_name',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = productt
        # exclude = ('user',)
        fields=['product_name','category_name','price','pic','Specification','purchased_year']


class SfeedbackForm(forms.ModelForm):
    class Meta:
        model = Cfeedback
        fields = ('feedback',)
