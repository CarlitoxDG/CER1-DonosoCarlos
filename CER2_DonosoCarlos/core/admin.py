from django.contrib import admin
from .models import Correspondencia, Residencia


# Register your models here.
@admin.register(Correspondencia)

class vistaAdmin(admin.ModelAdmin):
    search_fields= ('tipo', 'estado')
    list_display = ('id','tipo','estado')

@admin.register(Residencia)
class vistaAdmin2(admin.ModelAdmin):
    list_display = ('id','nombre_dueño', 'nroResidencia')
