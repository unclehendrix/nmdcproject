from django.contrib import admin
from .models import Department,Division,Unit,Staff
from django.contrib.auth.models import Group

admin.site.site_header = 'NMDC Dashboard'

class DepartmentAdmin(admin.ModelAdmin):
    list_display =('Department_Name',)

class DivisionAdmin(admin.ModelAdmin):
    list_display =['Division_Name','Department_Name']
    list_filter = ['Department_Name']
    
class UnitAdmin(admin.ModelAdmin):
    list_display =['Unit_Name','Department_Name']
    list_filter = ['Department_Name']
    
class StaffAdmin(admin.ModelAdmin):
    list_display =['Staff_Id','Staff_Name','Department_Name','Division_Name','Unit_Name','Section_Name',
                   'Date_First_app','Date_Present_app','Cadre',
                   'Rank_position','Gloconraiss','DOB','File_No',
                   'Geo_Political_zone','State','Local_Gov_Area','IPPS']
    
    list_filter = ['Staff_Id','Staff_Name']
        
# Register your models here.
admin.site.register(Staff,StaffAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Division,DivisionAdmin)
admin.site.register(Unit,UnitAdmin)