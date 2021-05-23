# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import AppointmentForm, PatientForm
from .models import Appointment, Patient

# @login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        if "book-an-appointment" in load_template:
            if request.method == 'POST':
                form = AppointmentForm(request.POST)
                if form.is_valid():
                    form.save()
                    html_template = loader.get_template('appointment-success.html')
                    return HttpResponse(html_template.render(context, request))
            else:
                form = AppointmentForm()
            context['form'] = form

        if "appointments" in load_template:
            if request.method == "POST":
                if 'complete' in request.POST:
                    pk = request.POST.get('complete')
                    appointment = Appointment.objects.get(pk=pk)
                    appointment.status = "Completed"
                    appointment.save()
                elif 'accept' in request.POST:
                    pk = request.POST.get('accept')
                    appointment = Appointment.objects.get(pk=pk)
                    appointment.status = "Accepted"
                    appointment.save()
                elif 'reject' in request.POST:
                    pk = request.POST.get('reject')
                    appointment = Appointment.objects.get(pk=pk)
                    appointment.status = "Rejected"
                    appointment.save()
                elif 'delete' in request.POST:
                    pk = request.POST.get('delete')
                    appointment = Appointment.objects.get(pk=pk)
                    appointment.delete()
            context['appointments'] = Appointment.objects.all()

        if "patients-info" in load_template:
            if request.method == "POST":
                if 'admit' in request.POST:
                    pk = request.POST.get('admit')
                    patient = Patient.objects.get(pk=pk)
                    patient.status = "Admitted"
                    patient.save()
                elif 'update' in request.POST:
                    pk = request.POST.get('update')
                    patient = Patient.objects.get(pk=pk)
                    form = PatientForm(instance=patient)
                    context['form'] = form
                    patient.delete()
                    html_template = loader.get_template('register-a-patient.html')
                    return HttpResponse(html_template.render(context, request))
                elif 'remove' in request.POST:
                    pk = request.POST.get('remove')
                    patient = Patient.objects.get(pk=pk)
                    patient.delete()
            context['patients'] = Patient.objects.all()

        if "register-a-patient" in load_template:
            if request.method == 'POST':
                form = PatientForm(request.POST)
                if form.is_valid():
                    form.save()
                    context['patients'] = Patient.objects.all()
                    html_template = loader.get_template('patients-info.html')
                    return HttpResponse(html_template.render(context, request))
            else:
                form = PatientForm()
            context['form'] = form

        if "iot-monitoring" in load_template:
            context["patient_exist"] = Patient.objects.filter(status="Admitted").exists()
            context["patients"] = Patient.objects.filter(status="Admitted")

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request), content_type="application/javascript")
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

