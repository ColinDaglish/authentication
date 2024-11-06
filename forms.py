# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Parent, Teacher


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ["phone_number", "address"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["subject", "phone_number"]
