from django import forms
from .models import Knowledge, Module, View, Attachment


class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['name']


class ViewForm(forms.ModelForm):

    class Meta:
        model = View
        fields = ['name', 'name_view', 'module', 'type', 'description']


class ErrorForm(forms.ModelForm):

    class Meta:
        model = Knowledge
        fields = ['title', 'view', 'description', 'decision']

class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['name', 'path']