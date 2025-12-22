from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from pricings.forms import FeaturesInlineFormSet, OurPricingForm
from pricings.models import OurPricings
from django.urls import reverse_lazy, reverse


class PricingUtils:
    def pricing_create_or_update(self, request, pk=None):
        if pk:
            # Update Operation
            pricing = get_object_or_404(OurPricings, pk=pk)

            # try:
            #     pricing = OurPricings.objects.get(pk=pk)
            # except Exception as e:
            #     raise Http404(
            #         "No %s matches the given query." % e.args
            #     )

        else:
            # Insert / Create Operation
            pricing = OurPricings() # object instantiation

        if request.method == "POST":
            pricing_form = OurPricingForm(request.POST, instance=pricing)
            formset = FeaturesInlineFormSet(request.POST, instance=pricing)

            if pricing_form.is_valid() and formset.is_valid():
                pricing = pricing_form.save()
                formset.instance = pricing
                formset.save()
                return redirect(self.success_url)  # change as needed
        else:
            pricing_form = OurPricingForm(instance=pricing)
            formset = FeaturesInlineFormSet(instance=pricing)

        return render(
            request,
            "custom-admin/form.html",
            {
                "pricing_form": pricing_form,
                "formset": formset,
            },
        )


class PricingList(generic.ListView):
    # queryset
    # model

    # template_name

    # model = OurPricings
    queryset = OurPricings.objects.all().order_by("-priority")
    template_name = "custom-admin/pricings.html"


class PricingCreate(generic.CreateView, PricingUtils):
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

    # request.GET
    def get(self, request, *args, **kwargs):
        return self.pricing_create_or_update(request)

    # request.POST
    def post(self, request, *args, **kwargs):
        return self.pricing_create_or_update(request)

    
class PricingEdit(generic.UpdateView,PricingUtils):
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

    def get(self, request, *args, **kwargs):
        # my_vls = {'pk': '4'}
        # => func(pk=my_vls["pk"])
        # func(**my_vls) 
        # => func(pk=4)

        return self.pricing_create_or_update(request, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.pricing_create_or_update(request, **kwargs)

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