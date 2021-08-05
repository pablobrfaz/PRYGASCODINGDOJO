# Generated by Django 3.2.3 on 2021-08-01 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasbravo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia_rem', models.CharField(max_length=30)),
                ('fecha_ingr', models.DateField(null=True)),
                ('cantidad_stock', models.IntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=4, default=0.0, max_digits=5, null=True)),
                ('precio_venta', models.DecimalField(decimal_places=4, default=0.0, max_digits=5, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unit', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('total_pedido', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('bodega_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasbravo.bodega')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prod', models.CharField(max_length=30)),
                ('peso', models.CharField(max_length=2)),
                ('tipo', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_fac', models.DateField(null=True)),
                ('sub_total', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('iva', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('total_factura', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('det_venta', models.ManyToManyField(through='gasbravo.Detalle_Venta', to='gasbravo.Bodega')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to='gasbravo.user')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='facturas_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasbravo.factura'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='prod_bod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_bod', to='gasbravo.producto'),
        ),
    ]
