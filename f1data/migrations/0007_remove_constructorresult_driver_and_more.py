# Generated by Django 4.0.4 on 2022-05-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f1data', '0006_remove_constructorstanding_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructorresult',
            name='driver',
        ),
        migrations.AddField(
            model_name='constructorresult',
            name='constructor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='f1data.constructor'),
        ),
        migrations.AddField(
            model_name='constructorstanding',
            name='constructor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='f1data.constructor'),
        ),
    ]