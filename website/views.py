from django.shortcuts import get_object_or_404, render

from .models import Service


def home(request):

    services = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        "website/home.html",
        {
            "services": services,
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