from django.contrib import admin
from .models import Unit, Workers, Visit
# Register your models here.

class UnitAdmin(admin.ModelAdmin):
    search_fields = ['name__startswith']


class WorkersAdmin(admin.ModelAdmin):
    search_fields = ['name__startswith']


class VisitAdmin(admin.ModelAdmin):
    search_fields = ['unit__name','unit__worker__name' ]


admin.site.register(Unit, UnitAdmin)
admin.site.register(Workers, WorkersAdmin)
admin.site.register(Visit, VisitAdmin)