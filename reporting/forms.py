from django.forms import ModelForm
from reporting.admin import UserCreationForm
from reporting.models import MyUser,Course,Batch
from django import forms


class UserAddForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=MyUser
        fields=['email','roll','password1','password2']
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.Select(attrs={'class':'form-control'})

        }

class CourseAddForm(ModelForm):
    class Meta:
        model=Course
        fields=['course_name','is_active']
        widgets={
            'course_name':forms.TextInput(attrs={'class':'form-control'}),

        }

class BatchAddForm(ModelForm):
    class Meta:
        model=Batch
        fields=['course','batch_name','is_active']
        widgets={
            'course':forms.Select(attrs={'class':'form-control'}),
            'batch_name':forms.TextInput(attrs={'class':'form-control'})
        }

