# Generated by Django 4.0.4 on 2022-05-26 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1data', '0008_rename_constructor_result_constructorresult_constructor_result_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='race',
            options={'ordering': ['-year', '-round']},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['-year']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='driverstanding',
            order_with_respect_to='race',
        ),
    ]
