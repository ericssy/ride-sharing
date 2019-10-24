from django.contrib import admin
from .models import Ride, Rider, Driver
from django.contrib.admin.views.main import ChangeList


# Register your models here.

admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Ride)

'''
class RideChangeList(ChangeList):

    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin, sortable_by):

        super(RideChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable,
            model_admin, sortable_by)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['action_checkbox', 'departure_location', 'destination_location', 'date', 'rider']
        self.list_display_links = ['rider']
        self.list_editable = ['rider']


class RideAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return RideChangeList

    def get_changelist_form(self, request, **kwargs):
        return RideChangeListForm

admin.site.register(Ride, RideAdmin)
'''
