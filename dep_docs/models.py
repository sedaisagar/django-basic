from django.db import models

from utils.models import CommonModel

# Create your models here.


class Departments(CommonModel):
    name = models.CharField(max_length=100)
    
    # published = models.BooleanField()
    # priority = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "departments"

    def __str__(self):
        return self.name

class Doctors(CommonModel):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)

    short_intro = models.TextField()

    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()

    image = models.ImageField(upload_to="doctors-image", null=True,blank=True)
    # published = models.BooleanField()
    # priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        app_counts = self.appointments.all().count()
        return f"{self.name} - Appointments ({app_counts})"

    class Meta:
        db_table = "doctors"