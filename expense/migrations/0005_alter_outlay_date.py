# Generated by Django 4.1.1 on 2022-10-08 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20221004_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlay',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 8, 16, 49, 13, 526627, tzinfo=datetime.timezone.utc)),
        ),
    ]
