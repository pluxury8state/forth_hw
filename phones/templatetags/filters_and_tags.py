from django.template import library

register = library.Library()


@register.filter
def exist(val: bool):
    if val:
        return 'есть'
    else:
        return 'нет'


@register.filter
def without_space(val: str):
    val = val.replace(' ', '-')
    return val
