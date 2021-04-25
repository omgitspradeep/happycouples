from django.urls import path
from .views import (
    home,
    index,
    getAllGuestData,
    )

urlpatterns = [
    path('<str:inviteeCode>/', index, name='index'),
    path('',home,name='home-rs'),
    path('api/getMyGuests/',getAllGuestData,name='get-all-guest-data-rs'),
]
