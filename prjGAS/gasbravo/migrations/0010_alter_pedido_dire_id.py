# Generated by Django 3.2.3 on 2021-08-15 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasbravo', '0009_auto_20210815_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='dire_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dire_id', to='gasbravo.direccion'),
        ),
    ]
