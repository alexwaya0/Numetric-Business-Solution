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