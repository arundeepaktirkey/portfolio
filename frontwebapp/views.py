from django.shortcuts import render
from .models import WorkExp, Education, MyServices, Internships, Projects
# Create your views here.
def home(request):
    workex = WorkExp.objects.all()
    educations = Education.objects.all()
    services = MyServices.objects.all()
    internships = Internships.objects.all()
    projects = Projects.objects.all()

    
    context = {
        'workexps': workex,
        'educations' : educations,
        'services' : services,
        'internships': internships,
        'projects': projects
        }
    return render(request, 'frontwebapp/home.html', context = context)
