import django_filters
from .models import TimeSheet,MyUser
from django import forms

class TimeFilter(django_filters.FilterSet):
    # batch=django_filters.ModelChoiceFilter(queryset=MyUser.objects.all(),widget=forms.Select(attrs={'class','form-class'}))
    date=django_filters.DateFilter(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=TimeSheet
        fields=['date','batch']




