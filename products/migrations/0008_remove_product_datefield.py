# Generated by Django 2.1.5 on 2020-01-14 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200115_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='datefield',
        ),
    ]
