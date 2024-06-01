from django import forms
from ..models import MyServices

class servicesforms(forms.ModelForm):
    class Meta:
        model = MyServices
        fields = '__all__'