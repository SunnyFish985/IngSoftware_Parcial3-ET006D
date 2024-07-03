from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Categoria, Transfer, Chofer, Ticket, DetalleTicket
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import TransferForm, ChoferForm, TicketForm, DetalleForm
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

def reserva(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        detalle_form = DetalleForm(request.POST)
        
        if ticket_form.is_valid() and detalle_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.fechaReserva = timezone.now()
            ticket.precio = 1500
            ticket.save()

            detalle_ticket = detalle_form.save(commit=False)
            detalle_ticket.ticket = ticket
            detalle_ticket.save()

            transfer = detalle_ticket.transfer
            if transfer.cantAsientos <= detalle_ticket.asientosReserva:
                transfer.disponible = False
            transfer.cantAsientos -= detalle_ticket.asientosReserva
            transfer.save()

            return redirect('detalle_ticket', pk=ticket.idTicket)
    else:
        ticket_form = TicketForm()
        detalle_form = DetalleForm()

    return render(request, 'reserva.html', {
        'ticket_form': ticket_form,
        'detalle_form': detalle_form,
    })

def detalle_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    
    return render(request, 'detalleTicket.html', {
        'ticket': ticket
    })

#class Reserva(View):
#    def get(self, request):
#        ticketF = TicketForm()
#        ticketDetalleF = DetalleForm()
#        return render(request, 'book_transfer.html', {
#            'ticketF': ticketF,
#            'ticketDetalleF': ticketDetalleF
#        })

#    def post(self, request):
#        ticketF = TicketForm(request.POST)
#        ticketDetalleF = DetalleForm(request.POST)
#        if ticketF.is_valid() and ticketDetalleF.is_valid():
#            ticket = ticketF.save(commit=False)
#            ticket.fechaReserva = timezone.now()
#            ticket.precio = 1500
#            ticket.save()

#            ticketDetalle= ticketDetalleF.save(commit=False)
#            ticketDetalle.ticket = ticket
#            ticketDetalle.save()

#            transfer = ticketDetalle.transfer
#            if transfer.cantAsientos <= ticketDetalle.asientosReserva:
#                transfer.disponible = False
#            transfer.cantAsientos -= ticketDetalle.asientosReserva
#            transfer.save()

#            return redirect('success_page')
#        return render(request, 'book_transfer.html', {
#            'ticketF': ticketF,
#            'ticketDetalleF': ticketDetalleF
#        })

