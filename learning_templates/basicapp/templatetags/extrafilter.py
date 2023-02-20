from django import template

register = template.Library()

def wow(v):
    return v+" wow"

register.filter('wow', wow)

@register.filter(name='mod')
def mod(v, arg):
    return int(v) % arg
