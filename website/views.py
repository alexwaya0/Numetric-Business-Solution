from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import ContactForm
from .models import (
    Category,
    Certification,
    ContactEnquiry,
    CoreValue,
    Post,
    ProfessionalAffiliation,
    Service,
    SiteSettings,
    Testimonial,
)


def get_site_settings():
    """Return the active company settings."""

    return (
        SiteSettings.objects
        .filter(is_active=True)
        .first()
    )


def get_common_context():
    """Return content shared across multiple website pages."""

    return {
        "site_settings": get_site_settings(),

        "services": (
            Service.objects
            .filter(is_active=True)
            .order_by("number")
        ),

        "core_values": (
            CoreValue.objects
            .filter(is_active=True)
            .order_by("number")
        ),

        "testimonials": (
            Testimonial.objects
            .filter(is_active=True)
            .order_by(
                "display_order",
                "-created_at",
            )
        ),

        "certifications": (
            Certification.objects
            .filter(is_active=True)
            .order_by(
                "display_order",
                "name",
            )
        ),

        "affiliations": (
            ProfessionalAffiliation.objects
            .filter(is_active=True)
            .order_by(
                "display_order",
                "name",
            )
        ),
    }
    

def home(request):
    """Render the website home page."""

    services = (
        Service.objects
        .filter(is_active=True)
        .order_by("number")
    )

    featured_posts = (
        Post.objects
        .filter(
            is_published=True,
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )
        .select_related("category")
        .order_by(
            "-is_featured",
            "-published_at",
        )[:3]
    )

    context = get_common_context()

    context.update(
        {
            "services": services,
            "featured_posts": featured_posts,
        }
    )

    return render(
        request,
        "website/home.html",
        context,
    )


def about(request):
    """Render the about page."""

    context = get_common_context()

    return render(
        request,
        "website/about.html",
        context,
    )


def services(request):
    """Render the services page."""

    services = (
        Service.objects
        .filter(is_active=True)
        .order_by("number")
    )

    context = get_common_context()

    context.update(
        {
            "services": services,
        }
    )

    return render(
        request,
        "website/services.html",
        context,
    )


def service_detail(request, slug):
    """Render an individual service page."""

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True,
    )

    related_services = (
        Service.objects
        .filter(is_active=True)
        .exclude(pk=service.pk)
        .order_by("number")
    )

    context = get_common_context()

    context.update(
        {
            "service": service,
            "related_services": related_services,
        }
    )

    return render(
        request,
        "website/service_detail.html",
        context,
    )


def blog(request):
    """
    Display published insights with optional category filtering.

    Articles are ordered newest first. When a category is supplied
    through the query string, only published articles belonging to
    that category are displayed.
    """

    published_posts = (
        Post.objects
        .filter(
            is_published=True,
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )
        .select_related(
            "category",
        )
    )

    selected_category = None

    category_slug = request.GET.get("category")

    if category_slug:
        selected_category = get_object_or_404(
            Category.objects.filter(
                is_active=True,
            ),
            slug=category_slug,
        )

        published_posts = published_posts.filter(
            category=selected_category,
        )

    posts = published_posts.order_by(
        "-published_at",
        "-pk",
    )

    categories = (
        Category.objects
        .filter(
            is_active=True,
            posts__is_published=True,
            posts__published_at__isnull=False,
            posts__published_at__lte=timezone.now(),
        )
        .distinct()
        .order_by(
            "name",
        )
    )

    context = get_common_context()

    context.update(
        {
            "posts": posts,
            "categories": categories,
            "selected_category": selected_category,
        }
    )

    return render(
        request,
        "website/blog.html",
        context,
    )


def post_detail(request, slug):
    """Render an individual insight."""

    post = get_object_or_404(
        Post.objects.select_related("category"),
        slug=slug,
        is_published=True,
        published_at__isnull=False,
        published_at__lte=timezone.now(),
    )

    related_posts = (
        Post.objects
        .filter(
            category=post.category,
            is_published=True,
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )
        .exclude(pk=post.pk)
        .select_related("category")
        .order_by("-published_at")[:3]
    )

    context = get_common_context()

    context.update(
        {
            "post": post,
            "related_posts": related_posts,
        }
    )

    return render(
        request,
        "website/post_detail.html",
        context,
    )


def contact(request):
    """
    Render the contact page and process contact enquiries.

    AJAX requests receive JSON responses. Normal browser requests
    receive the rendered contact page.
    """

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if not form.is_valid():
            if (
                request.headers.get("X-Requested-With")
                == "XMLHttpRequest"
            ):
                return JsonResponse(
                    {
                        "success": False,
                        "message": (
                            "Please correct the errors below "
                            "and try again."
                        ),
                        "errors": form.errors.get_json_data(),
                    },
                    status=400,
                )

            context = get_common_context()

            context.update(
                {
                    "form": form,
                }
            )

            return render(
                request,
                "website/contact.html",
                context,
            )

        full_name = form.cleaned_data["full_name"]
        company_name = form.cleaned_data["company_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        service = form.cleaned_data["service"]
        message = form.cleaned_data["message"]

        enquiry = ContactEnquiry.objects.create(
            full_name=full_name,
            company_name=company_name,
            email=email,
            phone=phone,
            service_required=service.name,
            message=message,
        )

        subject = (
            "New website enquiry — "
            f"{service.name}"
        )

        email_body = f"""
New enquiry received from the Numetric Business Solution website.

==================================================
CONTACT INFORMATION
==================================================

FULL NAME
{full_name}

COMPANY
{company_name or "Not provided"}

EMAIL
{email}

PHONE
{phone or "Not provided"}

==================================================
SERVICE REQUIRED
==================================================

{service.name}

==================================================
MESSAGE
==================================================

{message}

==================================================
ENQUIRY REFERENCE
==================================================

#{enquiry.pk}

==================================================
WEBSITE
==================================================

www.numetricbusiness.co.ke
"""

        email_message = EmailMessage(
            subject=subject,
            body=email_body.strip(),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            reply_to=[email],
        )

        email_message.send(
            fail_silently=False,
        )

        if (
            request.headers.get("X-Requested-With")
            == "XMLHttpRequest"
        ):
            return JsonResponse(
                {
                    "success": True,
                    "message": (
                        "Thank you. Your enquiry has been "
                        "submitted successfully. We will "
                        "get back to you shortly."
                    ),
                    "enquiry_id": enquiry.pk,
                }
            )

        context = get_common_context()

        context.update(
            {
                "form": ContactForm(),
                "submitted": True,
                "enquiry": enquiry,
            }
        )

        return render(
            request,
            "website/contact.html",
            context,
        )

    context = get_common_context()

    context.update(
        {
            "form": form,
        }
    )

    return render(
        request,
        "website/contact.html",
        context,
    )