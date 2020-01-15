# Generated by Django 2.1.5 on 2020-01-14 23:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200115_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.AddField(
            model_name='product',
            name='datefield',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 23, 30, 9, 294742, tzinfo=utc), null=True),
        ),
    ]
