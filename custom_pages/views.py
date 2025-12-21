from django.shortcuts import render, redirect

from custom_pages.forms import AppointmentForm
from dep_docs.models import Departments, Doctors
from services.models import Services
from django.contrib import messages


# / -> View -> accepts request -> processes the request -> returns response


def home_page(request):

    if request.method == "POST":
        # request.POST  => immutable

        data = request.POST.copy() # mutable 

        data.update(
            appointment_date = data["appointment_date"][:10],
            appointment_time = data["appointment_time"][:4],
        )
        form = AppointmentForm(data=data)
        if form.is_valid():
            form.save()
            messages.success(request, message="Appointment Booked Successfully!")
            return redirect("/?#appointment-box")
        else:
            messages.error(request, message="Your data is invalid!")
            print(form.errors)

    context = {}
    # 
    # 
        # Data Processing here

    # services = Services.objects.all()
    services = Services.objects.filter(published=True)

    doctors = Doctors.objects.filter(published=True).order_by("-priority")
    departments = Departments.objects.filter(published=True).order_by("-priority")

    context.update(
        objects = services,
        doctors = doctors,
        departments = departments,
        form = AppointmentForm(),
    )
    # ...
    # 
    return render(request,"index.html", context)
    
def about_page(request):
    context = {}
    # 
    # 
        # Data Processing here
    
    doctors = Doctors.objects.filter(published=True).order_by("-priority")
    context["objects"] = doctors
    # ...
    # 
    return render(request,"about.html", context)
    
def service_page(request):
    context = {}
    # 
    # 
        # Data Processing here
    # ...
    # 
    return render(request,"service.html", context)
    
def price_page(request):
    context = {}
    # 
    # 
        # Data Processing here
    # ...
    # 
    return render(request,"price.html", context)
    
def contact_page(request):
    context = {}
    # 
    # 
        # Data Processing here
    # ...
    # 
    return render(request,"contact.html", context)
    
    
def testimonials_page(request):
    context = {
        "name":"Bijan Thing",
    }
    # 
    # 
        # Data Processing here
    # ...
    # 
    return render(request,"testimonial.html", context)
    

# JSON Response End Point View

from django.http import JsonResponse
def service_api(*args):
    services = Services.objects.filter(published=True).order_by("-priority").values()
    # services = [i for i in services]
    
    data = list(services)
    return JsonResponse(data,safe=False)


