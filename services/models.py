from django.db import models

from utils.models import CommonModel

# Create your models here.
class Services(CommonModel):
    icon = models.ImageField(upload_to="service-icons")
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=255)

    # published = models.BooleanField()
    # priority = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "services"
        ordering = ("-priority",)

        verbose_name = "Service"
        verbose_name_plural = "Service(s)"


    