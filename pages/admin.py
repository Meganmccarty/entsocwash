from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import Meeting

class MeetingAdmin(ModelAdmin):
    model = Meeting
    menu_label = "Meetings"
    menu_icon = "pick"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "date", "meeting_details")
    search_fields = ("title", "date", "meeting_details")

modeladmin_register(MeetingAdmin)