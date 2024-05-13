from django import forms
from ..models import WorkExp

class WorkExpForm(forms.ModelForm):
    class Meta:
        model = WorkExp
        fields = '__all__'
