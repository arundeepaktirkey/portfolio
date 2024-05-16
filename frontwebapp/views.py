from django.shortcuts import render
from .models import WorkExp
# Create your views here.
def home(request):
    workex = WorkExp.objects.all()
    # get_count = WorkExp.objects.all().count() 
    context = {
        'workexps': workex,
        }
    return render(request, 'frontwebapp/home.html', context = context)