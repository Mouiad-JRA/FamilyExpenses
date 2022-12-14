# Generated by Django 4.1.1 on 2022-10-02 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_rename_outlay_type_outlay_outlay_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='outlay',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 2, 15, 18, 16, 376478, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='outlaytype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
