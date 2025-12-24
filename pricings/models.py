from django.db import models

from utils.models import CommonModel

# Create your models here.
class OurPricings(CommonModel):
    name = models.CharField(max_length=255)
    normal_price = models.DecimalField(max_digits=12,decimal_places=2)
    offer_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "our_pricings"

class Features(CommonModel):
    name = models.CharField(max_length=255) 
    pricing = models.ForeignKey(OurPricings,on_delete=models.CASCADE, related_name="features")

    class Meta:
        db_table = "pricing_features"

# Eager, Lazy