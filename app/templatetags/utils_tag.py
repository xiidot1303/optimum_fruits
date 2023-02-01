from django import template


register = template.Library()

@register.filter()
def index(l, i):
    return l[i]

@register.filter()
def is_even_number(number):
    if number != 0 and number%2 == 0:
        return True
    else:
        return False

@register.filter()
def is_long_column_for_category(loop):
    if loop % 4 == 0 or loop % 4 == 1:
        return True
    return False

@register.filter()
def six_elements(obj):
    return obj[:6]