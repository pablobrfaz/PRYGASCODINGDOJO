# Generated by Django 3.2.3 on 2021-08-15 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gasbravo', '0014_auto_20210815_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='ped_prod',
        ),
    ]
