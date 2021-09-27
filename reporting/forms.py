from django.forms import ModelForm
from reporting.admin import UserCreationForm
from reporting.models import MyUser,Course,Batch,TimeSheet
from django import forms


class UserAddForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=MyUser
        fields=['email','roll','password1','password2']
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.Select(attrs={'class':'form-select'})

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
            'course':forms.Select(attrs={'class':'form-select'}),
            'batch_name':forms.TextInput(attrs={'class':'form-control'})
        }

class UserSigninForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class TimeSheetForm(ModelForm):
    class Meta:
        model=TimeSheet
        fields=['batch','topic','topic_status']
        widgets={
            'batch':forms.Select(attrs={'class':'form-select'}),
            'topic':forms.TextInput(attrs={'class':'form-control'}),
            'topic_status':forms.Select(attrs={'class':'form-control'})
        }