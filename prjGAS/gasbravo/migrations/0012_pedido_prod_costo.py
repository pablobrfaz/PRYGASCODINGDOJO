# Generated by Django 3.2.3 on 2021-08-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasbravo', '0011_alter_pedido_stat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_prod',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]
