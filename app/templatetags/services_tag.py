from django import template
from app.services import language_service
# from app.models import *

register = template.Library()

@register.filter()
def string(request, text):
    text = str(text).lower()
    return language_service.get_string(text, request)

@register.filter()
def title_string(request, obj):
    user_lang = language_service.get_lang_by_ip(
        language_service.get_user_ip(request)
    )
    if user_lang == 0:
        return obj.title_ru
    elif user_lang == 1:
        return obj.title_en
    else:
        return ''
     

@register.filter()
def user_lang(request):
    ip = language_service.get_user_ip(request)
    return language_service.get_lang_by_ip(ip)

# @register.filter()
# def sub_categories(category):
