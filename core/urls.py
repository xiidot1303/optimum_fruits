from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from app.views import *


urlpatterns = [
    path('control/', admin.site.urls),
    re_path(r'^files/(?P<path>.*)$', get_file),
    
    # main
    path('', pages),
    path('<str:page>/', pages),
    path('change-lang/<int:lang>/', change_lang, name='change_lang'),

    path('category/<int:pk>/', category, name='category'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
