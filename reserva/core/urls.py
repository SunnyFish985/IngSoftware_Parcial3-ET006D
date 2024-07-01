from django.urls import path
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('logout/',views.cerrar,name='cerrar'),
    path('crearTransf/',views.crearT,name='crearT'),
    path('crearChofer/',views.crearC,name='crearC'),

]