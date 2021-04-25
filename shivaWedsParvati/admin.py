from django.contrib import admin
from django.contrib.admin import AdminSite
import csv
from django.http import HttpResponse
from .models import WisherSP, InviteeSP


# Class to implement action that get all records for us in csv file
class ExportCsvMixin:
	def export_url_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = ['Name','Address','URL']
		response = HttpResponse(content_type = 'text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([obj.name,obj.address,obj.URL()])
		return response
	#export_as_csv.short_description = "Export Selected"



# Register your models here.
#admin.site.register(InviteeSP)

@admin.register(InviteeSP)
class InviteeAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display=('id','name','gender','address','inviteStatus','inviteeMessage','siteVisited','URL')
    actions = ["export_url_as_csv"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        
        # Removes the delete_selected option from admin panel
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions



@admin.register(WisherSP)
class WisherAdmin(admin.ModelAdmin):
    list_display=('id','InviteeSP','wishes','posted')