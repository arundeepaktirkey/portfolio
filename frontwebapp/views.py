from django.shortcuts import render
from .models import WorkExp, Education
# Create your views here.
def home(request):
    workex = WorkExp.objects.all()
    educations = Education.objects.all()

    # get_count = WorkExp.objects.all().count() 
    context = {
        'workexps': workex,
        'educations' : educations
        }
    return render(request, 'frontwebapp/home.html', context = context)