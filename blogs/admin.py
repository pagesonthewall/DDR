from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    radio_fields = {'sex': admin.HORIZONTAL}

admin.site.register(Patient, PatientAdmin)

