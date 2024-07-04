from django.contrib import admin
from .models import Categoria, Transfer, Chofer, Ticket, DetalleTicket
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Transfer)
admin.site.register(Chofer)
admin.site.register(Ticket)
admin.site.register(DetalleTicket)