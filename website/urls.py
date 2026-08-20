from django.urls import path

from . import views


app_name = "website"


urlpatterns = [

    # ======================================================
    # HOME
    # ======================================================

    path(
        "",
        views.home,
        name="home",
    ),


    # ======================================================
    # ABOUT US
    # ======================================================

    path(
        "about/",
        views.about,
        name="about",
    ),


    # ======================================================
    # SERVICES
    # ======================================================

    path(
        "services/",
        views.services,
        name="services",
    ),

    path(
        "services/<slug:slug>/",
        views.service_detail,
        name="service_detail",
    ),


    # ======================================================
    # BLOG
    # ======================================================

    path(
        "blog/",
        views.blog,
        name="blog",
    ),

    path(
        "blog/<slug:slug>/",
        views.post_detail,
        name="post_detail",
    ),


    # ======================================================
    # CONTACT US
    # ======================================================

    path(
        "contact/",
        views.contact,
        name="contact",
    ),

]