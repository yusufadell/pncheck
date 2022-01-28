from django import forms

class FileFieldForm(forms.Form):
    image_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
