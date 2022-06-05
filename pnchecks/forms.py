from django import forms
from django.contrib.auth.models import User

class FileFieldForm(forms.Form):
    upload_image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={
            'multiple': True,
        }))
    class Meta:
        model = User
        fields = ("username",)