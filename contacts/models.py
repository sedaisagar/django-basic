from django.db import models

# from dep_docs.models import Departments
from utils.models import BaseModel

class Appointments(BaseModel):
    department = models.ForeignKey("dep_docs.Departments", on_delete=models.PROTECT, related_name="appointments")
    doctor = models.ForeignKey("dep_docs.Doctors",on_delete=models.PROTECT, related_name="appointments")

    name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()


    class Meta:
        db_table = "appointments"

    def __str__(self):
        return self.name

"""
    A:
        c(related_name="as"),d,e

    C:
        ...
        C.as
    D:
        ...
    E:
        ...
"""