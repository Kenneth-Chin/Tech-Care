# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

SPECIALTIES = [("1", "Neurology - Dr. Kenneth Chin Wei Yow"),
               ("2", "Cardiology - Dr. Aw Zhi Wei"),
               ("3", "Psychiatry - Dr. Leong Chee Kei"),
               ("4", "Radiology - Dr. Kelwin Chew"),
               ("5", "Dermatology - Dr. Tan Zhi Jun")]

GENDERS = [("M", "Male"),
           ("F", "Female"),
           ("O", "Others")]


class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    request_specialty = models.CharField(max_length=1, choices=SPECIALTIES, default="1")
    medical_concern = models.TextField()
    status = models.CharField(max_length=30, default="Pending")


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default="M")
    date_of_birth = models.DateField()
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)

    health_related_info = models.TextField()
    diagnosis = models.TextField()
    medical_record = models.TextField()
    doctor = models.CharField(max_length=1, choices=SPECIALTIES, default="1")

    status = models.CharField(max_length=30, default="Registered")

