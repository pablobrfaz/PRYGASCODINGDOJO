# Generated by Django 3.2.3 on 2021-08-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasbravo', '0003_auto_20210814_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]