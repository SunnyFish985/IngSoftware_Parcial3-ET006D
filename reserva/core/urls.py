from django.urls import path
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('logout/',views.cerrar,name='cerrar'),
    path('crearTransf/',views.crearT,name='crearT'),
    path('crearChofer/',views.crearC,name='crearC'),
    path('reservar/',views.reserva,name='reserva'),
    path('detalleTicket/<int:pk>/', views.detalle_ticket, name='detalle_ticket'),
    path('servicios/', views.servicios, name='servicios'),
]