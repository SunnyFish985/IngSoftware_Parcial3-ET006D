# Generated by Django 5.0.6 on 2024-07-02 21:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_transfer_idchofer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pNomP', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('pApeP', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('rut', models.CharField(max_length=12, verbose_name='RUT')),
                ('fechaReserva', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleTicket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('destino', models.CharField(max_length=255)),
                ('asientosReserva', models.IntegerField(default=1)),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.transfer')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ticket')),
            ],
        ),
    ]