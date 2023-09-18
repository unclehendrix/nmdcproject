from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Staff,Department,Division,Unit
from .forms import DepartmentForm,UnitForm,DivisionForm,StaffForm



# Create your views here.

#Data for Staff
@login_required
def index(request):
    return render(request,'dashboard/index.html')

@login_required
def staff(request):
    items = Staff.objects.all()
    context = {
        'items': items,
    }
    return render(request,'dashboard/staff.html',context)

#delete data
def staff_delete(request,pk):
    items = Staff.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('dashboard-staff')
    return render(request,'dashboard/staff_delete.html')

#update data
def staff_update(request,pk):
    item = Staff.objects.get(id=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-staff')
    else:
        form = StaffForm(instance=item)
    context ={
        'form':form
    }
    return render(request,'dashboard/division_update.html',context)

#Data for Management
@login_required
def management(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-management')
    else:
        form = StaffForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/management.html',context)

#Data for Department
@login_required
def department(request):
    items = Department.objects.all()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-department')
    else:
        form = DepartmentForm()
    context = {
        'items': items,
        'form':form,
    }
    return render(request,'dashboard/department.html',context)

#delete data
def department_delete(request,pk):
    items = Department.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('dashboard-department')
    return render(request,'dashboard/department_delete.html')

#update data
def department_update(request,pk):
    item = Department.objects.get(id=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-department')
    else:
        form = DepartmentForm(instance=item)
    context ={
        'form':form
    }
    return render(request,'dashboard/department_update.html',context)

#Data for Unit
@login_required
def unit(request):
    items = Unit.objects.all()
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-unit')
    else:
        form = UnitForm()
    context = {
        'items': items,
        'form':form,
    }
    return render(request,'dashboard/unit.html',context)

#delete data
def unit_delete(request,pk):
    items = Unit.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('dashboard-unit')
    return render(request,'dashboard/unit_delete.html')

#update data
def unit_update(request,pk):
    item = Unit.objects.get(id=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-unit')
    else:
        form = UnitForm(instance=item)
    context ={
        'form':form
    }
    return render(request,'dashboard/unit_update.html',context)


#Data for Division
@login_required
def division(request):
    #save data
    items = Division.objects.all()
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard-division')
    else:
        form = DivisionForm()
    context = {
        'items': items,
        'form':form
    }
    return render(request,'dashboard/division.html',context)

#delete data
def division_delete(request,pk):
    items = Division.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('dashboard-division')
    return render(request,'dashboard/division_delete.html')

#update data
def division_update(request,pk):
    item = Division.objects.get(id=pk)
    if request.method == 'POST':
        form = DivisionForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-division')
    else:
        form = DivisionForm(instance=item)
    context ={
        'form':form
    }
    return render(request,'dashboard/division_update.html',context)


def generate_pdf(request):
    # Retrieve the data you want to include in the PDF (replace with your own data retrieval logic)
    data = {
        'title': 'My PDF Title',
        'fields': 'fields',
    }

    # Render the template with the data
    html_template = 'dashboard/staff.html'
    response = render(request, html_template, data)

    # Create a PDF using WeasyPrint
    pdf_file = HTML(string=response.fields).write_pdf()

    # Create an HTTP response with the PDF content and content type
    response = HttpResponse(pdf_file, fields_type='application/pdf')
    response['Content-Disposition'] = 'filename="my_pdf.pdf"'

    return response