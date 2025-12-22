from django import forms
from django.forms import inlineformset_factory
from .models import OurPricings, Features

class OurPricingForm(forms.ModelForm):
    class Meta:
        model = OurPricings
        fields = ["name", "normal_price", "offer_price", "published"]


FeaturesInlineFormSet = inlineformset_factory(
    OurPricings,
    Features,
    fields=["name", "published"],
    extra=5,          # number of empty forms
    can_delete=True   # allow deleting features
)
