from django.contrib import admin

# Register your models here.
from registration.models import CustomUser

admin.site.register(CustomUser)
