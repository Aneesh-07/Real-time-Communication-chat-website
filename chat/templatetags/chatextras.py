from django import template

register = template.Library()


@register.filter(name = 'initials')
def initials(value):
    initial = ''
    
    for name in value.split(' '):
        if name and len(initial )< 3:
            initial += name[0].upper()
            
    
    return initial
        