from django.urls import path
from .views import (
    home,
    index,
    getAllGuestData,
    )

urlpatterns = [
    path('<str:inviteeCode>/', index, name='index-sp'),
    path('',home,name='home-sp'),
    path('api/getMyGuests/',getAllGuestData,name='get-all-guest-data-sp'),


]
