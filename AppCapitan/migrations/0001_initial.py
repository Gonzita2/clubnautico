# Generated by Django 4.2.9 on 2024-03-03 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppEmpleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique='true', verbose_name='Cedula')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('direccion', models.CharField(max_length=70, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=12, verbose_name='Telefono')),
                ('sexo', models.CharField(blank='false', choices=[('femenimo', 'Femenino'), ('masculino', 'Masculino')], max_length=12, null='false', verbose_name='Sexo')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('fecha_nto', models.DateField()),
                ('documentos1', models.FileField(blank=True, null=True, upload_to='documentos')),
                ('documentos2', models.FileField(blank=True, null=True, upload_to='documentos')),
                ('documentos3', models.FileField(blank=True, null=True, upload_to='documentos')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='capitanes')),
                ('ciudad', models.ForeignKey(blank='true', max_length=70, null='true', on_delete=django.db.models.deletion.CASCADE, to='AppEmpleados.municipios', verbose_name='Ciudad')),
                ('departamento', models.ForeignKey(blank='true', max_length=70, null='true', on_delete=django.db.models.deletion.CASCADE, to='AppEmpleados.departamento', verbose_name='Departamento')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
