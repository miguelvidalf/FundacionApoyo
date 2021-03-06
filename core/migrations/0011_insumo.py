# Generated by Django 4.0.5 on 2022-06-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('codigo', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombrein', models.CharField(max_length=80, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=80, verbose_name='Descripción')),
                ('punitario', models.CharField(max_length=80, verbose_name='Precio Unitario')),
                ('cantidad', models.CharField(max_length=10, verbose_name='Cantidad')),
                ('fcompra', models.DateField(verbose_name='Fecha de compra(DD/MM/YYYY')),
                ('estado', models.CharField(max_length=30, verbose_name='Estado')),
                ('proveedor', models.CharField(blank=True, max_length=80, verbose_name='Proveedor')),
            ],
        ),
    ]
