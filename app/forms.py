from django import forms
from .models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'request_specialty', 'medical_concern']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'email', 'contact_number', 'health_related_info', 'diagnosis', 'medical_record', 'doctor', 'status']