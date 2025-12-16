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
    
    # published = models.BooleanField()
    # priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "doctors"