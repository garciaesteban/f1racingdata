# Generated by Django 4.0.4 on 2022-05-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1data', '0003_alter_sprintresult_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='time',
            field=models.CharField(default='', max_length=255),
        ),
    ]
