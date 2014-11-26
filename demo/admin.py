from django.contrib import admin
import autocomplete_light
from .models import *

# Register your models here.
class SomethingAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(SomethingWithSchema)

admin.site.register(SomethingWithSchema, SomethingAdmin)
admin.site.register(Foobar)
