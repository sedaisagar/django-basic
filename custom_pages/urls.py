from django.urls import path, include

from custom_pages.c_views import PricingList,PricingCreate,PricingDelete, PricingEdit

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
    # Class Based Views
    path("pricings", PricingList.as_view(), name="pricings"),
    path("pricings/create/", PricingCreate.as_view(), name="pricings-create"),
    path("pricings/edit/<str:pk>/", PricingEdit.as_view(), name="pricings-edit"),
    path("pricings/delete/<str:pk>/", PricingDelete.as_view(), name="pricings-delete"),

    # APIs
    path("api/",include([
        path("services/",service_api,name="service-api"),
        # ....
    ])),
]


