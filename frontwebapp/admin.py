from django.contrib import admin

from .models import WorkExp, Education, MyServices, Internships, Image, Projects, Description

from .forms.workexpforms import WorkExpForm
from .forms.eduforms import eduform 
from .forms.servicesforms import servicesforms
from .forms.internshipsforms import InternshipsAdminForm
from .forms.projectsforms import ProjectAdminForm


# Register your models here.

class WorkExpAdmin(admin.ModelAdmin):
    form = WorkExpForm

class EduAdmin(admin.ModelAdmin):
    form = eduform

class ServicesAdmin(admin.ModelAdmin):
    form = servicesforms

class InternshipsAdmin(admin.ModelAdmin):
    form = InternshipsAdminForm

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

admin.site.register(WorkExp, WorkExpAdmin)
admin.site.register(Education,EduAdmin)
admin.site.register(MyServices,ServicesAdmin)

admin.site.register(Internships, InternshipsAdmin)
admin.site.register(Image)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Description)




