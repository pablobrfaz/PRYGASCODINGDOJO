# Generated by Django 3.2.3 on 2021-08-15 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasbravo', '0012_pedido_prod_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr_id', to='gasbravo.user'),
        ),
    ]
