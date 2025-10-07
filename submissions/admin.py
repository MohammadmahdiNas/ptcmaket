from django.contrib import admin
from .models import Contact, Apply, Order


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone_number")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "status", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone_number", "study_field")
    list_filter = ("status", "created_at", "education_degree", "study_field")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    list_editable = ("status",)  # تغییر سریع وضعیت از لیست
    fieldsets = (
        ("اطلاعات فردی", {
            "fields": ("first_name", "last_name", "email", "phone_number")
        }),
        ("تحصیلات", {
            "fields": ("education_degree", "study_field")
        }),
        ("رزومه و نامه انگیزشی", {
            "fields": ("resume", "cover_letter")
        }),
        ("وضعیت و زمان", {
            "fields": ("status", "created_at")
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("company_name", "activity_area", "email", "contact_number", "status", "created_at")
    search_fields = ("company_name", "activity_area", "email", "contact_number")
    list_filter = ("status", "created_at", "activity_area")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    list_editable = ("status",)

