# Generated by Django 5.0.6 on 2024-06-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('idChofer', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Chofer')),
                ('rut', models.IntegerField(verbose_name='Rut')),
                ('dv', models.CharField(max_length=1, verbose_name='Dígito verificador')),
                ('pNom', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('sNom', models.CharField(max_length=30, verbose_name='Segundo Nombre')),
                ('pApe', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('sApe', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
            ],
        ),
        migrations.AddField(
            model_name='transfer',
            name='disponible',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
