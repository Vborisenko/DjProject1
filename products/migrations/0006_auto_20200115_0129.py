# Generated by Django 2.1.5 on 2020-01-14 23:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 23, 29, 4, 938805, tzinfo=utc), null=True),
        ),
    ]