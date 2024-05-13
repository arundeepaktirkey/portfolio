from django.contrib import admin
from .models import WorkExp
from .forms.workexpforms import WorkExpForm

# Register your models here.

class WorkExpAdmin(admin.ModelAdmin):
    form = WorkExpForm

admin.site.register(WorkExp, WorkExpAdmin)
