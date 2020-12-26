from django.contrib import admin
from .models import(
    Wisher,
    Invitee,
    )

# Register your models here.
#admin.site.register(Invitee)

@admin.register(Wisher)
class WisherAdmin(admin.ModelAdmin):
    list_display=('id','Invitee','wishes','posted')

@admin.register(Invitee)
class WisherAdmin(admin.ModelAdmin):
    list_display=('id','name','gender','address','inviteStatus','inviteeMessage','siteVisited','URL')
    
    