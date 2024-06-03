from django.shortcuts import render, redirect

from .models import WorkExp, Education, MyServices, Internships, Projects
from .forms import contactsforms
# Create your views here.
def home(request):
    workex = WorkExp.objects.all()
    educations = Education.objects.all()
    services = MyServices.objects.all()
    internships = Internships.objects.all()
    projects = Projects.objects.all()

    if request.method == 'POST':
        form = contactsforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontwebapp/home.html')  # Replace 'success_url' with the desired URL name
    else:
        form = contactsforms()

    context = {
        'workexps': workex,
        'educations' : educations,
        'services' : services,
        'internships': internships,
        'projects': projects,
        'form': form
        }
    return render(request, 'frontwebapp/home.html', context = context)


