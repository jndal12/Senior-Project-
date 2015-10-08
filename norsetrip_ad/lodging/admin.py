from django.contrib import admin

# Register your models here.
from .models import Lodging

#make the Lodging app modifiable in the admin
admin.site.register(Lodging)
