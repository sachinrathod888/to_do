from django import forms
from myapp.models import RegisterForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = '__all__'