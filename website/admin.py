from django.contrib import admin

from .models import (
    Category,
    Post,
    Service,
)


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_editable = (
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_published",
        "is_featured",
        "published_at",
    )

    list_display_links = (
        "title",
    )

    list_editable = (
        "is_published",
        "is_featured",
    )

    list_filter = (
        "category",
        "is_published",
        "is_featured",
    )

    search_fields = (
        "title",
        "excerpt",
        "body",
    )

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

    date_hierarchy = "published_at"

    ordering = (
        "-published_at",
        "-created_at",
    )

    fieldsets = (

        (
            "Article",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "author",
                    "excerpt",
                    "body",
                )
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "published_at",
                    "is_published",
                    "is_featured",
                )
            },
        ),

        (
            "Featured Image",
            {
                "fields": (
                    "featured_image",
                )
            },
        ),

        (
            "SEO",
            {
                "fields": (
                    "seo_title",
                    "seo_description",
                ),
                "classes": (
                    "collapse",
                ),
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