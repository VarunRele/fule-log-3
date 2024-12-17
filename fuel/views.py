from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Log
from django.contrib.auth.decorators import login_required
from .forms import LogForm
from django.contrib import messages
import logging

def index(request: HttpRequest):
    logs = Log.objects.all().order_by('-created_at')
    return render(request, 'fuel/tabular.html', {'logs': logs})
    
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