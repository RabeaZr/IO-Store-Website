from django import template

register = template.Library()

@register.filter
def mul( value, arg ):
    try:
        value = float( value )
        arg = float( arg )
        if arg: return value * arg
    except: pass
    return ''