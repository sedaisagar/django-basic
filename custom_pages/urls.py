from django.urls import path, include

from custom_pages.views import (
    home_page,
    about_page,
    service_page,
    price_page,
    contact_page,
    testimonials_page,
    # APIs
    service_api,
)

urlpatterns = [
    path("",home_page,name="home-page"),
    path("about",about_page,name="about-page"),
    path("service",service_page,name="service-page"),
    path("price",price_page,name="price-page"),
    path("contact",contact_page,name="contact"),
    path("testimonials",testimonials_page,name="testimonials"),
    # APIs
    path("api/",include([
        path("services/",service_api,name="service-api"),
        # ....
    ])),
]
