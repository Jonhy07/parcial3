from django.contrib import admin
from .models import *

class CityAdmin(admin.ModelAdmin):
    fields = ('city_name',)
class TitleAdmin(admin.ModelAdmin):
    fields = ('title_name',)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('nombre_medicamento','employee_city','employee_title',)

admin.site.register(City, CityAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Medicamento, EmployeeAdmin)