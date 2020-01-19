# Generated by Django 2.1.5 on 2020-01-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('s_name', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('MANAGER', 'MANAGER'), ('developer', 'DEVELOPER'), ('teamlead', 'TEAMLEAD'), ('pm', 'PM'), ('hr', 'HR')], default='developer', max_length=10)),
                ('work_time', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('cost_in_hour', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10000000)),
            ],
        ),
    ]