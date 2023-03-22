from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *

from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

# ////////////////////////save data//////////////////////////
def EmployeeRegistrationForm(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data saved successfully!')
            return redirect('registration')
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


# //////////////////////////////show data////////////////////////////////
def registration_list(request):
    registrations = registration.objects.all()
    return render(request, 'registration_list.html', {'registrations': registrations})


            
# ////////////////////////////delete data//////////////////////////////////
def delete(request, empid):
  emp = registration.objects.get(id=empid)
  emp.delete()
  messages.info(request, "Delete data Successfully")
  return redirect('registration_list')            




# ///////////////////////////update data///////////////////////////////////
def update_my_model(request, id):
    my_model = get_object_or_404(registration, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES, instance=my_model)
        if form.is_valid():
            form.save()
            messages.info(request, "Update data Successfully")
            return redirect('registration_list')
    else:
        form = EmployeeForm(instance=my_model)
    return render(request, 'update.html', {'form2': form})