import zipfile

from django import forms
from django.core.exceptions import ValidationError


class NewGameForm(forms.Form):
    packaged_app_archive = forms.FileField(allow_empty_file=False)

    def clean_packaged_app_archive(self):
        if not zipfile.is_zipfile(self.cleaned_data['packaged_app_archive']):
            raise ValidationError('Packaged app must be a valid ZIP archive.')
        return self.cleaned_data['packaged_app_archive']
