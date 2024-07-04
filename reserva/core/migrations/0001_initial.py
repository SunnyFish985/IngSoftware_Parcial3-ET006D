# Generated by Django 5.0.6 on 2024-06-30 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Categoria')),
                ('nombreCategoria', models.CharField(max_length=40, verbose_name='Nombre Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('idVehiculo', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Id Vehículo')),
                ('patente', models.CharField(max_length=6, verbose_name='Patente')),
                ('cantAsientos', models.PositiveIntegerField(verbose_name='Cantidad de Asientos')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria', verbose_name='Categoria')),
            ],
        ),
    ]