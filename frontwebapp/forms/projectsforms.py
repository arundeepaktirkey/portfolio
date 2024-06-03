from django.contrib import admin

from django.forms import ModelMultipleChoiceField, ModelForm
from ..models import Projects, Description

class ProjectAdminForm(ModelForm):
    descriptions = ModelMultipleChoiceField(
        queryset=Description.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name='Descriptions',
            is_stacked=False
        )
    )

    class Meta:
        model = Projects
        fields = '__all__'

