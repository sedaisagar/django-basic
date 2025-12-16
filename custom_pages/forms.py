from django import forms

from contacts.models import Appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = "__all__"
        # fields = ["name", "email"]