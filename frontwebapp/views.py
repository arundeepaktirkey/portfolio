from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import WorkExp, Education, MyServices, Internships, Projects
from .forms.contactsforms import ContactForm

# Create your views here.
def home(request):
    workex = WorkExp.objects.all()
    educations = Education.objects.all()
    services = MyServices.objects.all()
    internships = Internships.objects.all()
    projects = Projects.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('')  # Replace 'success_url' with the desired URL name
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    context = {
        'workexps': workex,
        'educations' : educations,
        'services' : services,
        'internships': internships,
        'projects': projects,
        'form': form
        }
    return render(request, 'frontwebapp/home.html', context = context)


