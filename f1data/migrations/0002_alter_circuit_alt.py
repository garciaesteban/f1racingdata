# Generated by Django 4.0.4 on 2022-05-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuit',
            name='alt',
            field=models.IntegerField(null=True),
        ),
    ]