from django import template

register = template.Library()

@register.filter(name='as_form_control')
def as_form_control(value, arg):
    return value.as_widget(attrs={'placeholder': arg, 'class': 'form-control'})