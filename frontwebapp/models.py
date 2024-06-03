from django.db import models

# Create your models here.
class WorkExp(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)   
    description = models.TextField(max_length=500)
    skills = models.CharField(max_length=300)

    @property
    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    @property
    def formatted_end_date(self):
        if self.end_date:
            return self.end_date.strftime("%b %Y")
        else:
            return 'Present'
        
        
class Education(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)   
    description = models.TextField(max_length=500)
    skills = models.CharField(max_length=300)

    @property
    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    @property
    def formatted_end_date(self):
        if self.end_date:
            return self.end_date.strftime("%b %Y")
        else:
            return 'Present'

class MyServices(models.Model):
    icon =  models.CharField(max_length=20, blank=True)
    technology = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

class Internships(models.Model):
    web_link = models.CharField(max_length=100, blank=True, default='#')
    bg_img = models.ImageField(upload_to='internships_imgs/')
    images = models.ManyToManyField('Image', blank=True)

class Image(models.Model):
    image = models.ImageField(upload_to='internships_imgs/')

class Projects(models.Model):
    project_link = models.CharField(max_length=100, default='#')
    image_url = models.ImageField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) 
    title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    descriptions = models.ManyToManyField('Description', blank=True)

class Description(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
