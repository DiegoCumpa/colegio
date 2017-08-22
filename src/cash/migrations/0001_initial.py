# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 06:30
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):


    initial = True

    dependencies = [
        ('register', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id_caja', models.AutoField(primary_key=True, serialize=False)),
                ('colegio', models.ForeignKey(db_column='id_colegio', to='register.Colegio')),
                ('numero', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'caja',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='CajaCajero',
            fields=[
                ('id_movimiento', models.AutoField(primary_key=True, serialize=False)),
                ('personal_colegio', models.ForeignKey(db_column='id_personal_colegio', to='register.PersonalColegio')),
                ('caja', models.ForeignKey(db_column='id_caja', to='cash.Caja')),
                ('saldo', models.FloatField()),
                ('monto_apertura', models.FloatField()),
                ('monto_cierre', models.FloatField()),
                ('estado', models.IntegerField()),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'caja_cajero',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Remesa',
            fields=[
                ('id_remesa', models.AutoField(primary_key=True, serialize=False)),
                ('personal_colegio', models.ForeignKey(db_column='id_personal_colegio', to='register.PersonalColegio')),
                ('movimiento', models.ForeignKey(db_column='id_movimiento', to='cash.CajaCajero')),
                ('fechacreacion', models.DateTimeField()),
                ('monto', models.FloatField()),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'remesa',
                'managed': settings.IS_TESTING,
            },
        ),
    ]

