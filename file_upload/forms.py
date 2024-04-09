# file_upload/forms.py

from django import forms
from .models import UploadedFile
from django.contrib.auth.models import User



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class FileUploadForm(forms.ModelForm):
    file = MultipleFileField(label='Fayllarni Tanlang')
    allowed_users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label='Ko''ruvchi foydalanuvchilar')
    select_all_users = forms.BooleanField(initial=True, required=False, label='Barcha foydalanuvchini tanlash', widget=forms.CheckboxInput(attrs={'onclick': 'toggleUsers(this)'}))
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}),label='Qisqa Zametka')
    class Meta:
        model = UploadedFile
        fields = ['file','comment','allowed_users']
