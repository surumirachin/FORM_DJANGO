from django import forms
from django.forms import ValidationError
from . models import *


class StudentForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, required=True,)
    email = forms.EmailField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    classes = forms.ChoiceField(choices=standard , required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Student
        fields = [ 'full_name','email','age','classes','description']

  

  
       
