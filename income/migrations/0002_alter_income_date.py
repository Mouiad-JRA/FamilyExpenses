# Generated by Django 4.1.1 on 2022-10-08 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 8, 22, 49, 34, 2965, tzinfo=datetime.timezone.utc)),
        ),
    ]
