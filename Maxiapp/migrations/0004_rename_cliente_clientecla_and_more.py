# Generated by Django 5.0.6 on 2024-06-01 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maxiapp', '0003_rename_producto_proveedor_rubro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='ClienteCla',
        ),
        migrations.RenameModel(
            old_name='Empleado',
            new_name='EmpleadoCla',
        ),
        migrations.RenameModel(
            old_name='Proveedor',
            new_name='ProveedorCla',
        ),
    ]