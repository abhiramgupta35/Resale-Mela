import django_filters
from django import forms
from django_filters import CharFilter

from .models import *


class ServiceFilter(django_filters.FilterSet):
    product_name = CharFilter(field_name='product_name', label="Search Product",lookup_expr='icontains',widget=forms.TextInput(attrs={
            'placeholder': 'Search Product Name ', 'class':'form-control'}))


    class Meta:
        model = productt
        fields = ('product_name',)



