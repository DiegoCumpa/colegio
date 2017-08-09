# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
                     ('register','0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id_tipo_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('colegio', models.ForeignKey(db_column='id_colegio',to='register.Colegio')),
                ('is_ordinario', models.BooleanField()),
                ('nivel', models.IntegerField(blank=True, null=True)),
                ('grado', models.IntegerField(blank=True, null=True)),
                ('extra', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo_modular', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('usuario_creacion', models.CharField(max_length=10,null=True)),
                ('usuario_modificacion', models.CharField(max_length=10,null=True)),
            ],
            options={
                'db_table': 'tipo_servicio',
                'managed': settings.IS_TESTING
                #'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('is_periodic', models.BooleanField()),
                ('fecha_facturar', models.DateField()),
                ('cuotas', models.IntegerField()),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('usuario_creacion', models.CharField(max_length=10,null=True)),
                ('usuario_modificacion', models.CharField(max_length=10,null=True)),
                ('tipo_servicio', models.ForeignKey(db_column='id_tipo_servicio', to='enrollment.TipoServicio')),
            ],
            options={
                'db_table': 'servicio',
                'managed': settings.IS_TESTING
                #'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id_matricula', models.AutoField(primary_key=True)),
                ('alumno', models.ForeignKey(db_column='id_alumno',to='register.Alumno')),
                ('colegio', models.ForeignKey(db_column='id_colegio',to='register.Colegio')),
                ('tipo_servicio', models.ForeignKey(db_column='id_tipo_servicio',to='enrollment.TipoServicio')),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'matricula',
                'managed': settings.IS_TESTING
                # 'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuentascobrar',
            fields=[
                ('id_cuentascobrar', models.AutoField(primary_key=True)),
                ('matricula', models.ForeignKey(db_column='id_matricula', to='enrollment.Matricula')),
                ('servicio', models.ForeignKey(db_column='id_servicio', to='enrollment.Servicio')),
                ('fecha_ven', models.DateField()),
                ('comentario', models.CharField(max_length=500, blank=True, null=True)),
                ('estado', models.BooleanField()),
                ('precio', models.FloatField()),
                ('deuda', models.FloatField()),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'cuentascobrar',
                'managed': settings.IS_TESTING
                # 'managed': False,
            },
        ),
    ]