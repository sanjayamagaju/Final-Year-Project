from django.contrib import admin
from django.contrib.auth.models import Group
from .models import FuturePurpose, Gallery, OtherCampaign, LeaderBoard


# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Image', 'Target', 'Collected', 'Info')
    list_display_links = ('id', 'Name')
    list_editable = ('Info',)
    list_per_page = 10
    search_fields = ('Name', 'Info')
    list_filter = ('Name', 'Date_added')

class FupAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'amount')
    list_display_links = ('id', 'token', 'amount')
    list_per_page = 10

class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'donor', 'donation_amt', 'camp_detail')
    list_display_links = ('id', 'token', 'donor')
    list_per_page = 10


admin.site.register(OtherCampaign, CampaignAdmin)
admin.site.unregister(Group)
admin.site.register(Gallery)
admin.site.register(FuturePurpose, FupAdmin)
admin.site.register(LeaderBoard, LeaderboardAdmin)