from django import forms
from ..models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }
        help_texts = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Enter your email address',
            'subject': 'Enter the subject of your message',
            'message': 'Enter your message',
        }
        widgets = {
            'first_name': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'last_name': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'email': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'subject': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'message': forms.Textarea(attrs={'rows': 5, 'cols': 70}),
        }
