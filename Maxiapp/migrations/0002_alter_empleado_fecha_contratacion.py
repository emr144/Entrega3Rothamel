# Generated by Django 5.0.6 on 2024-06-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maxiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_contratacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]