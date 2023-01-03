from django import forms
from .models import Archive

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = ['filiere', 'semester']
        
    def __init__(self, *args, **kwargs):
        super(ArchiveForm, self).__init__(*args, **kwargs)
        self.fields['filiere'].widget.attrs={
            'id': 'filiere',
            }
        self.fields['semester'].widget.attrs={
            'id': 'semester',
            }