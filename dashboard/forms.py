from django import forms
from.models import Department,Unit,Division,Staff

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Department_Name']
        
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['Unit_Name','Department_Name']
        
class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['Division_Name','Department_Name']
        
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['Staff_Id','Staff_Name','Department_Name','Division_Name','Unit_Name','Section_Name','Date_First_app',
                  'Date_Present_app','Cadre',
                  'Rank_position','Gloconraiss',
                  'DOB','File_No','Geo_Political_zone','State','Local_Gov_Area','IPPS']


