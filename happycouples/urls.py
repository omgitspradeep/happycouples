from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import hblog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rs/',include('ramWedsSita.urls')),
    path('sp/',include('shivaWedsParvati.urls')),
    path('blogs/', hblog, name='hindu-blog'),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

'''
API:

https://happycouples.herokuapp.com/rs/api/getMyGuests/

'''