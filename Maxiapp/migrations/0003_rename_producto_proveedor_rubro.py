# Generated by Django 5.0.6 on 2024-06-01 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maxiapp', '0002_alter_empleado_fecha_contratacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='producto',
            new_name='rubro',
        ),
    ]
