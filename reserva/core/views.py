from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Categoria, Transfer, Chofer
from django.contrib.auth.models import User
from .forms import TransferForm, ChoferForm
# Create your views here.
def admin_test(user):
    return user.is_authenticated and user.is_staff

def index(request):
    return render(request, 'index.html')

def cerrar(request):
    logout(request)
    return redirect('index')


@user_passes_test(admin_test)
@login_required
def crearT(request):
    if request.method == 'POST':
        transform = TransferForm(request.POST, request.FILES)
        if transform.is_valid():
            transform.save()
            return redirect('index')
    else:
        transform = TransferForm()
    return render(request,'crearTransfer.html', {'transform':transform})

@user_passes_test(admin_test)
@login_required
def crearC(request):
    if request.method == 'POST':
        choferform = ChoferForm(request.POST)
        if choferform.is_valid():
            choferform.save()
            return redirect('index')
    else:
        choferform = ChoferForm()
    return render(request, 'crearChofer.html', {'chofer_form': choferform})

