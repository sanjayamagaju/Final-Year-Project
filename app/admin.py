from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Campaign
from .models import OtherCampaign
from .models import Gallery

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Image', 'Target', 'Collected', 'Info')
    list_display_links = ('id', 'Name')
    list_editable = ('Info',)
    list_per_page = 10
    search_fields = ('Name', 'Info')
    list_filter = ('Name', 'Date_added')


admin.site.register(Campaign)
admin.site.register(OtherCampaign, CampaignAdmin)
admin.site.unregister(Group)
admin.site.register(Gallery)
