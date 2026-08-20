from django.db import models
from django.urls import reverse


# ==========================================================
# SERVICE
# ==========================================================

class Service(models.Model):

    name = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        unique=True
    )

    number = models.PositiveIntegerField(
        unique=True
    )

    tagline = models.CharField(
        max_length=255
    )

    overview = models.TextField()

    services = models.TextField(
        help_text="Enter one service per line."
    )

    who_its_for = models.TextField(
        verbose_name="Who it's for"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "number"
        ]

        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name

    def get_services_list(self):

        return [
            item.strip()
            for item in self.services.splitlines()
            if item.strip()
        ]

    def get_absolute_url(self):

        return reverse(
            "website:service_detail",
            kwargs={
                "slug": self.slug
            }
        )


# ==========================================================
# BLOG CATEGORY
# ==========================================================

class Category(models.Model):

    name = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        unique=True
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            "name"
        ]

        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):

        return self.name


# ==========================================================
# BLOG POST
# ==========================================================

class Post(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts"
    )

    title = models.CharField(
        max_length=220
    )

    slug = models.SlugField(
        unique=True
    )

    excerpt = models.TextField(
        max_length=500
    )

    body = models.TextField(
        help_text=(
            "Write the article body. "
            "Separate paragraphs with blank lines."
        )
    )

    featured_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True
    )

    author = models.CharField(
        max_length=150,
        default="Numetric Business Solution"
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    is_published = models.BooleanField(
        default=False
    )

    is_featured = models.BooleanField(
        default=False
    )

    seo_title = models.CharField(
        max_length=220,
        blank=True
    )

    seo_description = models.CharField(
        max_length=320,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "-published_at",
            "-created_at",
        ]

        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse(
            "website:post_detail",
            kwargs={
                "slug": self.slug
            }
        )

    @property
    def display_title(self):

        return self.seo_title or self.title

    @property
    def display_description(self):

        return (
            self.seo_description
            or self.excerpt
        )

    @property
    def paragraphs(self):

        return [
            paragraph.strip()
            for paragraph in self.body.split("\n\n")
            if paragraph.strip()
        ]


# ==========================================================
# SITE SETTINGS
# ==========================================================

class SiteSettings(models.Model):

    """
    Stores the main company and website information.

    This is intentionally a singleton-style model.
    Only one active settings record should normally exist.
    """

    company_name = models.CharField(
        max_length=200,
        default="Numetric Business Solution"
    )

    tagline = models.CharField(
        max_length=255,
        blank=True
    )

    logo = models.ImageField(
        upload_to="branding/",
        blank=True,
        null=True
    )

    email = models.EmailField(
        default="info@numetricbusiness.co.ke"
    )

    managing_partner_email = models.EmailField(
        default="managing.partner@numetricbusiness.co.ke"
    )

    accounts_email = models.EmailField(
        default="accounts@numetricbusiness.co.ke"
    )

    phone = models.CharField(
        max_length=50,
        default="0739 651 744"
    )

    office_location = models.CharField(
        max_length=255,
        default="Mombasa Road, Vision Plaza"
    )

    website = models.URLField(
        default="https://www.numetricbusiness.co.ke"
    )

    mission = models.TextField(
        blank=True
    )

    vision = models.TextField(
        blank=True
    )

    about_intro = models.TextField(
        blank=True
    )

    about_body = models.TextField(
        blank=True
    )

    facebook_url = models.URLField(
        blank=True
    )

    instagram_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    twitter_url = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):

        return self.company_name


# ==========================================================
# CORE VALUE
# ==========================================================

class CoreValue(models.Model):

    number = models.PositiveIntegerField(
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        ordering = [
            "number"
        ]

        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):

        return self.name


# ==========================================================
# TESTIMONIAL
# ==========================================================

class Testimonial(models.Model):

    quote = models.TextField()

    name = models.CharField(
        max_length=150,
        blank=True
    )

    role = models.CharField(
        max_length=150,
        blank=True
    )

    company = models.CharField(
        max_length=150,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            "display_order",
            "-created_at",
        ]

        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):

        if self.name:
            return self.name

        return "Testimonial"


# ==========================================================
# CERTIFICATION
# ==========================================================

class Certification(models.Model):

    name = models.CharField(
        max_length=150
    )

    logo = models.ImageField(
        upload_to="certifications/",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "display_order",
            "name",
        ]

        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):

        return self.name


# ==========================================================
# PROFESSIONAL AFFILIATION
# ==========================================================

class ProfessionalAffiliation(models.Model):

    name = models.CharField(
        max_length=200
    )

    logo = models.ImageField(
        upload_to="affiliations/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "display_order",
            "name",
        ]

        verbose_name = "Professional Affiliation"
        verbose_name_plural = "Professional Affiliations"

    def __str__(self):

        return self.name


# ==========================================================
# CONTACT ENQUIRY
# ==========================================================

class ContactEnquiry(models.Model):

    full_name = models.CharField(
        max_length=150
    )

    company_name = models.CharField(
        max_length=200,
        blank=True
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    service_required = models.CharField(
        max_length=200
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            "-created_at"
        ]

        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"

    def __str__(self):

        return f"{self.full_name} — {self.email}"