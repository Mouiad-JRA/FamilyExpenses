# Generated by Django 3.2 on 2022-10-04 16:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_alter_material_name_alter_outlay_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlay',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 16, 8, 30, 373056, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outlay',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
