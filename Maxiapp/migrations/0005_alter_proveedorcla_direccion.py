# Generated by Django 5.0.6 on 2024-06-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maxiapp', '0004_rename_cliente_clientecla_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedorcla',
            name='direccion',
            field=models.TextField(max_length=100),
        ),
    ]
