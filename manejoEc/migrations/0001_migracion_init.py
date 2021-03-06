# Generated by Django 3.2.7 on 2021-10-15 18:17

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaModel',
            fields=[
                ('marcaId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('marcaNombre', models.CharField(db_column='nombre', max_length=100)),
                ('marcaDescripcion', models.TextField(null=True)),
            ],
            options={
                'db_table': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('productoId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('productoNombre', models.CharField(db_column='nombre', max_length=100)),
                ('productoPrecio', models.DecimalField(db_column='precio', decimal_places=2, max_digits=5)),
                ('productoFoto', models.CharField(db_column='foto', max_length=130, null=True)),
                ('productoCantidad', models.IntegerField(db_column='cantidad', validators=[django.core.validators.MinValueValidator(0, 'Valor no puede ser negativo')])),
                ('productoTalla', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), db_column='talla', size=None), size=None)),
                ('productoActualizado', models.DateTimeField(auto_now_add=True, db_column='updated_at')),
                ('productoCreado', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('marca', models.ForeignKey(db_column='marca_id', on_delete=django.db.models.deletion.PROTECT, related_name='marcaProducto', to='manejoEc.marcamodel')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuarioId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('usuarioDni', models.CharField(db_column='dni', max_length=8)),
                ('usuarioNombre', models.CharField(db_column='nombre', max_length=50)),
                ('usuarioApellido', models.CharField(db_column='apellido', max_length=50, verbose_name='Apellido del usuario')),
                ('usuarioCorreo', models.EmailField(db_column='email', max_length=50, unique=True)),
                ('usuarioTipo', models.IntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'OPERARIO'), (3, 'CLIENTE')], db_column='tipo')),
                ('password', models.TextField(null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
