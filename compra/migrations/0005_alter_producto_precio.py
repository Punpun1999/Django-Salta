# Generated by Django 4.2.1 on 2023-05-14 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_producto_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]