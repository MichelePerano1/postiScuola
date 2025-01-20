from django import template

register = template.Library()

@register.filter
def modulo(value, divisor):
    """Returns the remainder of the division `value % divisor`."""
    return value % divisor

@register.filter
def index(List, i):
    """Access the list element by index."""
    try:
        return List[int(i)]
    except:
        return None