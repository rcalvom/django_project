from django import forms

from app.models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file')
