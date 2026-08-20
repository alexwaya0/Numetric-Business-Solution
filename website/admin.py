from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from .models import (
    Service,
    Category,
    Post,
    SiteSettings,
    CoreValue,
    Testimonial,
    Certification,
    ProfessionalAffiliation,
    ContactEnquiry,
)


# ==========================================================
# ADMIN SITE BRANDING
# ==========================================================

admin.site.site_header = "Numetric Business Solution"

admin.site.site_title = "Numetric Business Solution"

admin.site.index_title = "Business Management"


# ==========================================================
# REMOVE GROUPS FROM ADMIN
# ==========================================================

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass


# ==========================================================
# SERVICE ADMIN
# ==========================================================

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
        "services",
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
            "Service Content",
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

    save_on_top = True


# ==========================================================
# BLOG CATEGORY ADMIN
# ==========================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "is_active",
        "created_at",
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
        "description",
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }

    ordering = (
        "name",
    )

    fieldsets = (

        (
            "Category",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "is_active",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),

    )

    readonly_fields = (
        "created_at",
    )


# ==========================================================
# BLOG POST ADMIN
# ==========================================================

@admin.action(description="Publish selected articles")
def publish_posts(modeladmin, request, queryset):

    queryset.update(
        is_published=True
    )


@admin.action(description="Unpublish selected articles")
def unpublish_posts(modeladmin, request, queryset):

    queryset.update(
        is_published=False
    )


@admin.action(description="Feature selected articles")
def feature_posts(modeladmin, request, queryset):

    queryset.update(
        is_featured=True
    )


@admin.action(description="Remove articles from Featured")
def unfeature_posts(modeladmin, request, queryset):

    queryset.update(
        is_featured=False
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "author",
        "publication_status",
        "featured_status",
        "published_at",
    )

    list_display_links = (
        "title",
    )

    list_filter = (
        "category",
        "is_published",
        "is_featured",
        "published_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "body",
        "author",
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

    actions = (
        publish_posts,
        unpublish_posts,
        feature_posts,
        unfeature_posts,
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
            "Search Engine Optimisation",
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

    save_on_top = True

    @admin.display(
        description="Status",
        ordering="is_published",
    )
    def publication_status(self, obj):

        if obj.is_published:

            return format_html(
                '<span style="'
                'color:#1B6B3A;'
                'font-weight:600;'
                '">'
                'Published'
                '</span>'
            )

        return format_html(
            '<span style="'
            'color:#777;'
            'font-weight:600;'
            '">'
            'Draft'
            '</span>'
        )

    @admin.display(
        description="Featured",
        boolean=True,
        ordering="is_featured",
    )
    def featured_status(self, obj):

        return obj.is_featured


# ==========================================================
# SITE SETTINGS ADMIN
# ==========================================================

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "email",
        "phone",
        "office_location",
        "is_active",
        "updated_at",
    )

    list_display_links = (
        "company_name",
    )

    list_editable = (
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "company_name",
        "tagline",
        "email",
        "phone",
        "office_location",
    )

    fieldsets = (

        (
            "Company Identity",
            {
                "fields": (
                    "company_name",
                    "tagline",
                    "logo",
                    "website",
                )
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "managing_partner_email",
                    "accounts_email",
                    "phone",
                    "office_location",
                )
            },
        ),

        (
            "About the Business",
            {
                "fields": (
                    "about_intro",
                    "about_body",
                    "mission",
                    "vision",
                )
            },
        ),

        (
            "Social Media",
            {
                "fields": (
                    "facebook_url",
                    "instagram_url",
                    "linkedin_url",
                    "twitter_url",
                )
            },
        ),

        (
            "Website Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),

    )

    readonly_fields = (
        "updated_at",
    )

    save_on_top = True


# ==========================================================
# CORE VALUES ADMIN
# ==========================================================

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "name",
        "description",
        "is_active",
    )

    list_display_links = (
        "name",
    )

    list_editable = (
        "number",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "number",
    )

    fieldsets = (

        (
            "Core Value",
            {
                "fields": (
                    "number",
                    "name",
                    "description",
                    "is_active",
                )
            },
        ),

    )


# ==========================================================
# TESTIMONIAL ADMIN
# ==========================================================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "quote_preview",
        "name",
        "role",
        "company",
        "is_active",
        "display_order",
    )

    list_display_links = (
        "quote_preview",
    )

    list_editable = (
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "quote",
        "name",
        "role",
        "company",
    )

    ordering = (
        "display_order",
        "-created_at",
    )

    fieldsets = (

        (
            "Testimonial",
            {
                "fields": (
                    "quote",
                )
            },
        ),

        (
            "Client Information",
            {
                "fields": (
                    "name",
                    "role",
                    "company",
                )
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                    "display_order",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),

    )

    readonly_fields = (
        "created_at",
    )

    @admin.display(
        description="Testimonial"
    )
    def quote_preview(self, obj):

        if len(obj.quote) > 80:

            return f"{obj.quote[:80]}..."

        return obj.quote


# ==========================================================
# CERTIFICATION ADMIN
# ==========================================================

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "is_active",
        "display_order",
    )

    list_display_links = (
        "name",
    )

    list_editable = (
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "display_order",
        "name",
    )

    fieldsets = (

        (
            "Certification",
            {
                "fields": (
                    "name",
                    "logo",
                    "description",
                )
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                    "display_order",
                )
            },
        ),

    )


# ==========================================================
# PROFESSIONAL AFFILIATION ADMIN
# ==========================================================

@admin.register(ProfessionalAffiliation)
class ProfessionalAffiliationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "website",
        "is_active",
        "display_order",
    )

    list_display_links = (
        "name",
    )

    list_editable = (
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "display_order",
        "name",
    )

    fieldsets = (

        (
            "Affiliation",
            {
                "fields": (
                    "name",
                    "logo",
                    "website",
                    "description",
                )
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                    "display_order",
                )
            },
        ),

    )


# ==========================================================
# CONTACT ENQUIRY ADMIN
# ==========================================================

@admin.action(description="Mark selected enquiries as read")
def mark_enquiries_read(modeladmin, request, queryset):

    queryset.update(
        is_read=True
    )


@admin.action(description="Mark selected enquiries as unread")
def mark_enquiries_unread(modeladmin, request, queryset):

    queryset.update(
        is_read=False
    )


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "company_name",
        "email",
        "phone",
        "service_required",
        "read_status",
        "created_at",
    )

    list_display_links = (
        "full_name",
    )

    list_filter = (
        "is_read",
        "service_required",
        "created_at",
    )

    search_fields = (
        "full_name",
        "company_name",
        "email",
        "phone",
        "service_required",
        "message",
    )

    date_hierarchy = "created_at"

    ordering = (
        "-created_at",
    )

    actions = (
        mark_enquiries_read,
        mark_enquiries_unread,
    )

    fieldsets = (

        (
            "Contact Information",
            {
                "fields": (
                    "full_name",
                    "company_name",
                    "email",
                    "phone",
                )
            },
        ),

        (
            "Enquiry",
            {
                "fields": (
                    "service_required",
                    "message",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_read",
                )
            },
        ),

        (
            "Received",
            {
                "fields": (
                    "created_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),

    )

    readonly_fields = (
        "created_at",
    )

    @admin.display(
        description="Status",
        ordering="is_read",
    )
    def read_status(self, obj):

        if obj.is_read:

            return format_html(
                '<span style="'
                'color:#777;'
                'font-weight:600;'
                '">'
                'Read'
                '</span>'
            )

        return format_html(
            '<span style="'
            'color:#1B6B3A;'
            'font-weight:700;'
            '">'
            'New'
            '</span>'
        )


# ==========================================================
# ADMIN INTERFACE CONFIGURATION
# ==========================================================

admin.site.empty_value_display = "—"