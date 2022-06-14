# Generated by Django 4.0.5 on 2022-06-14 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_insumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='descripcion',
            field=models.TextField(max_length=80, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='fcompra',
            field=models.DateField(verbose_name='Fecha de Compra'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60, verbose_name='Titulo')),
                ('encargado', models.CharField(max_length=60, verbose_name='Encargado')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.CharField(max_length=8, verbose_name='Hora')),
                ('anotacion', models.TextField(verbose_name='Anotacion')),
                ('residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
    ]
