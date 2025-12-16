from django.contrib import admin

# Register your models here.
from dep_docs.models import Departments,Doctors

admin.site.register([Departments,Doctors])