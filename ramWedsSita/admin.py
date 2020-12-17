from django.contrib import admin
from .models import Wisher

# Register your models here.
#admin.site.register(WisherAdmin)

@admin.register(Wisher)
class WisherAdmin(admin.ModelAdmin):
    list_display=('id','name','wishes','posted')