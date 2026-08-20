from django.conf import settings
from django.core.mail import send_mail
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


# ==========================================================
# SHARED WEBSITE DATA
# ==========================================================

def get_site_settings():
    """
    Return the active company settings.

    The website normally uses one active SiteSettings record.
    """

    return (
        SiteSettings.objects
        .filter(is_active=True)
        .first()
    )


def get_common_context():
    """
    Content shared across multiple website pages.
    """

    return {
        "site_settings": get_site_settings(),

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


# ==========================================================
# HOME
# ==========================================================

def home(request):

    services = (
        Service.objects
        .filter(
            is_active=True,
        )
        .order_by(
            "number",
        )
    )

    featured_posts = (
        Post.objects
        .filter(
            is_published=True,
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )
        .select_related(
            "category",
        )
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


# ==========================================================
# ABOUT
# ==========================================================

def about(request):

    context = get_common_context()

    return render(
        request,
        "website/about.html",
        context,
    )


# ==========================================================
# SERVICES
# ==========================================================

def services(request):

    services = (
        Service.objects
        .filter(
            is_active=True,
        )
        .order_by(
            "number",
        )
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


# ==========================================================
# SERVICE DETAIL
# ==========================================================

def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True,
    )

    related_services = (
        Service.objects
        .filter(
            is_active=True,
        )
        .exclude(
            pk=service.pk,
        )
        .order_by(
            "number",
        )
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


# ==========================================================
# BLOG
# ==========================================================

def blog(request):

    posts = (
        Post.objects
        .filter(
            is_published=True,
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )
        .select_related(
            "category",
        )
        .order_by(
            "-published_at",
        )
    )

    categories = (
        Category.objects
        .filter(
            is_active=True,
        )
        .order_by(
            "name",
        )
    )

    context = get_common_context()

    context.update(
        {
            "posts": posts,
            "categories": categories,
        }
    )

    return render(
        request,
        "website/blog.html",
        context,
    )


# ==========================================================
# BLOG POST DETAIL
# ==========================================================

def post_detail(request, slug):

    post = get_object_or_404(
        Post.objects.select_related(
            "category",
        ),
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
        .exclude(
            pk=post.pk,
        )
        .select_related(
            "category",
        )
        .order_by(
            "-published_at",
        )[:3]
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


# ==========================================================
# CONTACT
# ==========================================================

def contact(request):

    form = ContactForm()

    if request.method == "POST":

        form = ContactForm(
            request.POST
        )

        if form.is_valid():

            full_name = form.cleaned_data[
                "full_name"
            ]

            company_name = form.cleaned_data[
                "company_name"
            ]

            email = form.cleaned_data[
                "email"
            ]

            phone = form.cleaned_data[
                "phone"
            ]

            service = form.cleaned_data[
                "service"
            ]

            message = form.cleaned_data[
                "message"
            ]

            # ==================================================
            # SAVE ENQUIRY
            # ==================================================

            enquiry = ContactEnquiry.objects.create(
                full_name=full_name,
                company_name=company_name,
                email=email,
                phone=phone,
                service_required=service.name,
                message=message,
            )

            # ==================================================
            # EMAIL NOTIFICATION
            # ==================================================

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

            send_mail(
                subject=subject,
                message=email_body.strip(),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[
                    settings.CONTACT_EMAIL,
                ],
                reply_to=[
                    email,
                ],
                fail_silently=False,
            )

            # ==================================================
            # SUCCESS
            # ==================================================

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

    # ======================================================
    # INITIAL / INVALID FORM
    # ======================================================

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