# Generated by Django 4.0.4 on 2022-05-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1data', '0004_alter_result_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]