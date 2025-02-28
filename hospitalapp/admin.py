from django.contrib import admin
from hospitalapp.models import *

# Register your models here.

admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(staff)
admin.site.register(ward)
admin.site.register(appointment)
admin.site.register(contact)
