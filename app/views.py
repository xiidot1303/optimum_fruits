from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, HttpResponse
from app.models import *
from app.utils import *
from app.services.language_service import *

def pages(request, page='index'):
    categories = Category.objects.all()
    products = Product.objects.all()
    photos = Photo.objects.all()[:6]
    context = {
        'page': page, 'products': products, 'categories': categories, 'photos': photos, 
        }
    return render(request, f'{page}.html', context)

def change_lang(request, lang):
    ip = get_user_ip(request)
    update_lang_by_ip(ip, int(lang))
    return redirect(request.META.get('HTTP_REFERER'))

def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    context = {'categories': categories, 'obj': category}
    return render(request, 'category.html', context)


def get_file(request, path):
    file = open(f'files/{path}', 'rb')
    return FileResponse(file)