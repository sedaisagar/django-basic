from django.views import generic

from pricings.models import OurPricings
from django.urls import reverse_lazy, reverse


class PricingList(generic.ListView):
    # queryset
    # model

    # template_name

    # model = OurPricings
    queryset = OurPricings.objects.all().order_by("-priority")
    template_name = "custom-admin/pricings.html"


class PricingCreate(generic.CreateView):
    # queryset
    # model

    # template_name
    # fields

    model = OurPricings
    template_name = "custom-admin/form.html"
    # fields = "__all__"
    fields = ["name","normal_price","offer_price","published"]

    success_url = reverse_lazy("pricings")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        
        data.update(
            title = "Create Pricing"
        )
        return data

class PricingEdit(generic.UpdateView):
    # queryset
    # model

    # template_name
    # fields

    model = OurPricings
    template_name = "custom-admin/form.html"
    fields = "__all__"
    # fields = ["name","normal_price","offer_price","published"]

    success_url = reverse_lazy("pricings")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)

        data.update(
            title = "Edit Pricing ? ",
            show_object = False,
        )
 
        return data

class PricingDelete(generic.DeleteView):
    # queryset
    # model

    # template_name
    # fields

    model = OurPricings
    template_name = "custom-admin/form.html"
    success_url = reverse_lazy("pricings")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)

        data.update(
            title = "Delete This Pricing Object ? ",
            show_object = True,
        )
 
        return data