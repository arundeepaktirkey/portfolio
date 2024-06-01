from django.contrib import admin

from django.forms import ModelMultipleChoiceField, ModelForm
from ..models import Internships, Image

class InternshipsAdminForm(ModelForm):
    images = ModelMultipleChoiceField(
        queryset=Image.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name='Images',
            is_stacked=False
        )
    )

    class Meta:
        model = Internships
        fields = '__all__'