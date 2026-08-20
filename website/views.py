from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import ContactForm
from .models import Post, Service, Category


def home(request):

    services = Service.objects.filter(
        is_active=True
    )

    featured_posts = (
        Post.objects
        .filter(
            is_published=True,
            published_at__lte=timezone.now(),
        )
        .select_related("category")
        .order_by(
            "-is_featured",
            "-published_at",
        )[:3]
    )

    return render(
        request,
        "website/home.html",
        {
            "services": services,
            "featured_posts": featured_posts,
        },
    )


def about(request):

    return render(
        request,
        "website/about.html",
    )


def services(request):

    services = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        "website/services.html",
        {
            "services": services,
        },
    )


def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True,
    )

    return render(
        request,
        "website/service_detail.html",
        {
            "service": service,
        },
    )


def blog(request):

    posts = (
        Post.objects
        .filter(
            is_published=True,
            published_at__lte=timezone.now(),
        )
        .select_related("category")
    )

    return render(
        request,
        "website/blog.html",
        {
            "posts": posts,
        },
    )


def post_detail(request, slug):

    post = get_object_or_404(
        Post.objects.select_related("category"),
        slug=slug,
        is_published=True,
        published_at__lte=timezone.now(),
    )

    related_posts = (
        Post.objects
        .filter(
            category=post.category,
            is_published=True,
            published_at__lte=timezone.now(),
        )
        .exclude(
            pk=post.pk
        )
        .select_related("category")
        .order_by("-published_at")[:3]
    )

    return render(
        request,
        "website/post_detail.html",
        {
            "post": post,
            "related_posts": related_posts,
        },
    )


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

            subject = (
                "New website enquiry — "
                f"{service.name}"
            )

            email_body = f"""
New enquiry received from the Numetric website.

FULL NAME
{full_name}

COMPANY
{company_name or "Not provided"}

EMAIL
{email}

PHONE
{phone}

SERVICE REQUIRED
{service.name}

MESSAGE
{message}
"""

            send_mail(
                subject=subject,
                message=email_body.strip(),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[
                    settings.CONTACT_EMAIL,
                ],
                fail_silently=False,
            )

            return render(
                request,
                "website/contact.html",
                {
                    "form": ContactForm(),
                    "submitted": True,
                },
            )

    return render(
        request,
        "website/contact.html",
        {
            "form": form,
        },
    )





