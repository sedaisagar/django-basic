from django.contrib import admin

# Register your models here.
from pricings.models import OurPricings,Features

admin.site.register([OurPricings,Features])