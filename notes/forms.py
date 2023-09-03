from django import forms
from .models import Notes,Comments
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model= Notes
        fields=["title","subject","university", "notesfile","description","tags"]

        widgets={
            "title": forms.TextInput(attrs={'class': "form-control"}),
            "subject": forms.TextInput(attrs={'class': "form-control"}),
            "university": forms.TextInput(attrs={'class': "form-control"}),
            "tags": forms.TextInput(attrs={'class': "form-control"}),
            "description": forms.Textarea(attrs={'class': "form-control","width": "100%"}),
            "notesfile":forms.FileInput(attrs={'class': 'form-control-file'})
        }

    def clean(self):
        cleaned_data=self.cleaned_data
        notesfile=self.files.get('notesfile')
        if(notesfile):
            filetype=notesfile.name.split('.')[1].upper()
            if not filetype=="PDF":
                raise ValidationError("Filetype not Supported, Please upload any one of these filetypes - 1. PDF\n 2. MP4\n")
        return cleaned_data