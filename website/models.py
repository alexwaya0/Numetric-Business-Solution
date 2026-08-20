from django.db import models
from django.urls import reverse


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
        help_text="Write the article body. Separate paragraphs with blank lines."
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

    def get_absolute_url(self):

        return reverse(
            "website:post_detail",
            kwargs={
                "slug": self.slug
            }
        )