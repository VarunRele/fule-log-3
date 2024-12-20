from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse
from .models import Log, Vehicle
from django.contrib.auth.decorators import login_required
from .forms import LogForm
from django.contrib import messages
from django.forms.models import model_to_dict
import logging

def index(request: HttpRequest):
    logs = Log.objects.all().order_by('-created_at')
    cars = Vehicle.objects.all()
    return render(request, 'fuel/tabular.html', {'logs': logs, 'cars': cars})
    
@login_required
def insert(request: HttpRequest):
    if request.method == 'POST':
        l_form = LogForm(request.POST)
        if l_form.is_valid():
            instance: Log = l_form.save(commit=False)
            instance.payee = request.user
            instance.save()
            messages.success(request, 'Log added')
            return redirect('fuel:index')
    else:
        l_form = LogForm()
    return render(request, 'fuel/insert.html', {'l_form': l_form, 'current_page': 'insert'})


@login_required
def edit_log(request: HttpRequest, pk: int):
    log_value = get_object_or_404(Log, pk=pk)
    l_form = LogForm(instance=log_value)
    if request.method == "POST":
        l_form = LogForm(request.POST, instance=log_value)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, 'You log updated successfully')
            return redirect('fuel:index')
    return render(request, 'fuel/edit_log.html', {'l_form': l_form})


@login_required
def delete_log(request: HttpRequest, pk: int):
    log_value = get_object_or_404(Log, pk=pk)
    log_value.delete()
    return redirect('fuel:index')


def fuel_logs_api(request: HttpRequest):
    selected_car = request.GET.get('car', 'all')
    if selected_car == 'all':
        logs = Log.objects.all()
    else:
        logs = Log.objects.filter(vehicle__id=selected_car)
    values = [model_to_dict(x) for x in logs]
    return JsonResponse(values, safe=False)