from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "name",
        "is_active",
        "updated_at",
    )

    list_display_links = (
        "name",
    )

    list_editable = (
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "tagline",
        "overview",
        "who_its_for",
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }

    ordering = (
        "number",
    )

    fieldsets = (

        (
            "Service Identity",
            {
                "fields": (
                    "name",
                    "slug",
                    "number",
                    "is_active",
                )
            },
        ),

        (
            "Content",
            {
                "fields": (
                    "tagline",
                    "overview",
                    "services",
                    "who_its_for",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),

    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )