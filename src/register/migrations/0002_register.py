# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        #('register', '0001_initial'),
    ]

    operations = [

        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id_colegio', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=11)),
                ('ugel', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'colegio',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("personal_create", "crear un personal"),
                    ("personal_detail", "verificar el detalle"),
                    ("personal_update", "actualizar el personal"),
                    ("personal_delete", "eliminar un personal"),
                    ("personal_list", "listar personal"),
                ),
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id_telefono', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('tipo', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
                ('id_persona', models.ForeignKey(db_column='id_persona', to='profiles.Profile', null=True, blank=True)),
                ('id_colegio', models.ForeignKey(db_column='id_colegio', to='register.Colegio', null=True, blank=True)),
                ('usuario_creacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Creacion')),
                ('usuario_modificacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Modificacion')),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True))
            ],
            options={
                'db_table': 'telefono',
                'managed': settings.IS_MIGRATE,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100, null=True)),
                ('dpto', models.CharField(max_length=15, null=True)),
                ('provincia', models.CharField(max_length=15, null=True)),
                ('distrito', models.CharField(max_length=100, null=True)),
                ('numero', models.CharField(max_length=6, null=True)),
                ('referencia', models.CharField(max_length=500, null=True)),
                ('id_persona', models.ForeignKey(db_column='id_persona', to='profiles.Profile', null=True, blank=True)),
                ('id_colegio', models.ForeignKey(db_column='id_colegio', to='register.Colegio', null=True, blank=True)),
                ('usuario_creacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Creacion')),
                ('usuario_modificacion',
                 models.CharField(blank=True, max_length=10, null=True, verbose_name='Usuario_Modificacion')),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True))
            ],
            options={
                'db_table': 'direccion',
                'managed': settings.IS_MIGRATE,
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('codigoint', models.CharField(blank=True, max_length=15, null=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                 parent_link=True, to='profiles.Profile')),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))

            ],
            options={
                'db_table': 'alumno',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("alumno_create", "crear alumno"),
                    ("alumno_detail", "detalle alumno"),
                    ("alumno_delete", "eliminar alumno"),
                    ("alumno_update", "actualizar alumno"),
                    ("alumno_list", "listar alumnos"),
                )
            },
            bases=('profiles.profile', models.Model),
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id_apoderado', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=30)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                 parent_link=True, to='profiles.Profile')),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'apoderado',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("apoderado_create", "crear apoderado"),
                    ("apoderado_detail", "detalle del apoderado"),
                    ("apoderado_update", "actualizar apoderado"),
                    ("apoderado_delete", "eliminiar un apoderado"),
                    ("apoderado_list", "listar apoderados")
                )
            },
            bases=('profiles.profile', models.Model),
        ),
        migrations.CreateModel(
            name='ApoderadoAlumno',
            fields=[
                ('id_apoderadoalumno', models.AutoField(auto_created=True, primary_key=True,
                                                        serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(db_column='id_alumno', to='register.Alumno')),
                ('apoderado', models.ForeignKey(db_column='id_apoderado', to='register.Apoderado')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))

            ],
            options={
                'db_table': 'apoderado_alumno',
                'managed': settings.IS_MIGRATE,
                'unique_together': (('alumno', 'apoderado'),)

            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_personal', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                 parent_link=True, to='profiles.Profile')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'personal',
                'managed': settings.IS_MIGRATE,
                'permissions': (("personal_create", "crear un personal"),
                    ("personal_detail", "verificar el detalle"),
                    ("personal_update", "actualizar el personal"),
                    ("personal_delete", "eliminar un personal"),
                    ("personal_list", "listar personal"),)
            },
        ),
        migrations.CreateModel(
            name='Sistemas',
            fields=[
                ('id_sistemas', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                  parent_link=True, to='register.Personal')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'sistemas',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("sistemas_create", "crear usuario sistemas"),
                    ("sistemas_update", "update usuario sistemas"),
                    ("sistemas_delete", "eliminar usuario sistemas"),
                    ("sistemas_list", "listar usuario sistemas"),
                    ("sistemas_detail", "detalle usuario sistemas"),
                )
            },
        ),
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('id_promotor', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                  parent_link=True, to='register.Personal')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'promotor',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("promotor_create", "crear promotor"),
                    ("promotor_update", "update promotor"),
                    ("promotor_delete", "eliminar promotor"),
                    ("promotor_list", "listar promotor"),
                    ("promotor_detail", "detalle promotor"),
                )
            },
        ),
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('id_cajero', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                      parent_link=True, to='register.Personal')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'cajero',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("cajero_create", "crear cajero"),
                    ("cajero_update", "update cajero"),
                    ("cajero_delete", "eliminar cajero"),
                    ("cajero_list", "listar cajero"),
                    ("cajero_detail", "detalle cajero"),
                )
            },
        ),
        migrations.CreateModel(
            name='Tesorero',
            fields=[
                ('id_tesorero', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                        parent_link=True, to='register.Personal')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'tesorero',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("tesorero_create", "crear tesorero"),
                    ("tesorero_update", "update tesorero"),
                    ("tesorero_delete", "eliminar tesorero"),
                    ("tesorero_list", "listar tesorero"),
                    ("tesorero_detail", "detalle tesorero"),
                )
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id_director', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING,
                                                        parent_link=True, to='register.Personal')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))
            ],
            options={
                'db_table': 'director',
                'managed': settings.IS_MIGRATE,
                'permissions': (
                    ("director_create", "crear director"),
                    ("director_update", "update director"),
                    ("director_delete", "eliminar director"),
                    ("director_list", "listar director"),
                    ("director_detail", "detalle director"),
                )
            },
        ),
        migrations.CreateModel(
            name='PersonalColegio',
            fields=[
                ('id_personal_colegio', models.AutoField(auto_created=True, primary_key=True,
                                                        serialize=False, verbose_name='ID')),
                ('personal', models.ForeignKey(db_column='id_personal', to='register.Personal')),
                ('colegio', models.ForeignKey(db_column='id_colegio', to='register.Colegio')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))

            ],
            options={
                'db_table': 'personal_colegio',
                'managed': settings.IS_MIGRATE,
                'unique_together': (('personal', 'colegio'),)

            },
        ),
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('usuario_creacion_administrativo',
                 models.CharField(blank=True, db_column='usuario_creacion', max_length=10, null=True,
                                  verbose_name='Usuario_Creacion')),
                ('usuario_modificacion_administrativo',
                 models.CharField(blank=True, db_column='usuario_modificacion', max_length=10, null=True,
                                  verbose_name='Usuario_Modificacion')),
                ('fecha_creacion_administrativo',
                 models.DateTimeField(blank=True, db_column='fecha_creacion', null=True)),
                ('fecha_modificacion_administrativo',
                 models.DateTimeField(blank=True, db_column='fecha_modificacion', null=True)),
                ('id_administrativo', models.AutoField(primary_key=True, serialize=False)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True,
                                                  to='register.Personal')),
                ('activo_administrativo', models.BooleanField(db_column='activo', default=True)),
            ],
            options={
                'db_table': 'administrativo',
                'managed': True,
                'permissions': (
                    ("administrativo_create", "crear administrativo"),
                    ("administrativo_update", "update administrativo"),
                    ("administrativo_delete", "eliminar administrativo"),
                    ("administrativo_list", "listar administrativo"),
                    ("administrativo_detail", "detalle administrativo"),
                )
            },
            bases=('register.personal', models.Model),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=15)),
                ('usuario_creacion_proveedor',
                 models.CharField(blank=True, db_column='usuario_creacion', max_length=10, null=True,
                                  verbose_name='Usuario_Creacion')),
                ('usuario_modificacion_proveedor',
                 models.CharField(blank=True, db_column='usuario_modificacion', max_length=10, null=True,
                                  verbose_name='Usuario_Modificacion')),
                ('fecha_creacion_proveedor', models.DateTimeField(blank=True, db_column='fecha_creacion', null=True)),
                ('fecha_modificacion_proveedor',
                 models.DateTimeField(blank=True, db_column='fecha_modificacion', null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': True,
                'permissions': (
                    ("proveedor_create", "crear proveedor"),
                    ("proveedor_update", "update proveedor"),
                    ("proveedor_delete", "eliminar proveedor"),
                    ("proveedor_list", "listar proveedor"),
                    ("proveedor_detail", "detalle proveedor"),
                )
            },
        ),
        migrations.CreateModel(
            name='ProveedorColegio',
            fields=[
                ('id_proveedor_colegio', models.AutoField(auto_created=True, primary_key=True,
                                                         serialize=False, verbose_name='ID')),
                ('proveedor', models.ForeignKey(db_column='id_proveedor', to='register.Proveedor')),
                ('colegio', models.ForeignKey(db_column='id_colegio', to='register.Colegio')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_creacion', models.CharField(max_length=10, null=True)),
                ('usuario_modificacion', models.CharField(max_length=10, null=True))

            ],
            options={
                'db_table': 'proveedor_colegio',
                'managed': settings.IS_MIGRATE,
            },
        ),

    ]


