from django.contrib import admin
from .models import WorkExp, Education
from .forms.workexpforms import WorkExpForm
from .forms.eduforms import eduform 

# Register your models here.

class WorkExpAdmin(admin.ModelAdmin):
    form = WorkExpForm

class EduAdmin(admin.ModelAdmin):
    form = eduform

admin.site.register(WorkExp, WorkExpAdmin)
admin.site.register(Education,EduAdmin)
