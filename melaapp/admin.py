from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.sellregister)
admin.site.register(models.productt)
admin.site.register(models.CustomerRequest)
