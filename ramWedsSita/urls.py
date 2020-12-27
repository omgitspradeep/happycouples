from django.urls import path
from .views import (
    home,
    index,
    )

urlpatterns = [
    path('<str:inviteeCode>/', index, name='index'),
    path('',home,name='home'),

]
