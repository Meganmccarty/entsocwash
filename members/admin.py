from django.contrib import admin

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import User, Member, Phone, Subject, Taxonomy, Geography

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'phone_type')

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0

@admin.register(Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ['taxon']

class TaxonomyInline(admin.TabularInline):
    model = Taxonomy
    extra = 0

@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    list_display = ['geography']

class GeographyInline(admin.TabularInline):
    model = Geography
    extra = 0

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    inlines = [PhoneInline, SubjectInline, TaxonomyInline, GeographyInline]


class MembershipAdmin(ModelAdmin):
    model = Member
    menu_label = "Members"
    menu_icon = "user"
    menu_order = 295
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("user", "first_name", "last_name", "address1")
    search_fields = ("user", "first_name", "last_name", "address1")
    

modeladmin_register(MembershipAdmin)