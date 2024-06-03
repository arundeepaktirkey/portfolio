from django import template
from django.forms import TextInput, Textarea

register = template.Library()

@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder):
    if isinstance(field.field.widget, TextInput):
        attrs = field.field.widget.attrs
        attrs.update({'placeholder': placeholder})
        field.field.widget.attrs = attrs
    elif isinstance(field.field.widget, Textarea):
        attrs = field.field.widget.attrs
        attrs.update({'placeholder': placeholder})
        field.field.widget.attrs = attrs
    return field
