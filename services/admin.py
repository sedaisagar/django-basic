from django.contrib import admin

from services.models import Services

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title","icon", "priority", "published"]


admin.site.register(Services,ServiceAdmin)