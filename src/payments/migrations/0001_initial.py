# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register','0002_register'),
        #('register', '0003_auto_20170826_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='CajaChica',
            fields=[
                ('id_caja_chica', models.AutoField(primary_key=True, serialize=False)),
                ('presupuesto', models.FloatField()),
                ('saldo', models.FloatField()),
                ('periodo', models.IntegerField()),
                ('colegio', models.ForeignKey(db_column='id_colegio', on_delete=django.db.models.deletion.DO_NOTHING, related_name='caja_chica', to='register.Colegio')),
                ('usuario_creacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Creacion')),
                ('usuario_modificacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Modificacion')),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                #'db_table': 'caja_chica',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('monto', models.FloatField()),
                ('fecha', models.DateTimeField()),
                ('numero_comprobante', models.CharField(max_length=30)),
                ('caja_chica', models.ForeignKey(db_column='id_caja_chica', on_delete=django.db.models.deletion.DO_NOTHING, related_name='pagos', to='payments.CajaChica')),
                ('personal', models.ForeignKey(db_column='id_personal_colegio', on_delete=django.db.models.deletion.DO_NOTHING, related_name='pagos', to='register.PersonalColegio')),
                ('proveedor', models.ForeignKey(db_column='id_proveedor_colegio', on_delete=django.db.models.deletion.DO_NOTHING, to='register.ProveedorColegio')),
                ('usuario_creacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Creacion')),
                ('usuario_modificacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Modificacion')),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                #'db_table': 'pago',
                'managed': True,
                'permissions': (
                    ('control_pagos', 'Para el control de pagos realizados'),
                    ("Registrar_Pago_Create", "crear registro de pago"),
                )
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tipo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('colegio', models.ForeignKey(db_column='id_colegio', to='register.Colegio')),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('padre', models.ForeignKey(db_column='id_parent', on_delete=django.db.models.deletion.DO_NOTHING, to='payments.TipoPago', blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
            options={
                #'db_table': 'tipo_pago',
                'managed': True,
                'permissions': (
                    ("Tipo_Pago_List", "ver lista de tipo de pago"),
                    ("Tipo_Pago_Detail", "ver detalle de tipo de pago"),
                    ("Tipo_Pago_Update", "modificar tipo de pago"),
                    ("Tipo_Pago_Creation", "crear tipo de pago"),
                    ("Tipo_Pago_Delete", "eliminar tipo de pago"),
                )
            },
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo_pago',
            field=models.ForeignKey(db_column='id_tipo_pago', on_delete=django.db.models.deletion.DO_NOTHING, related_name='pagos', to='payments.TipoPago'),
        ),
    ]
