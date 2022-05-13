# Generated by Django 4.0.4 on 2022-05-13 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuit_id', models.IntegerField()),
                ('circuit_ref', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('alt', models.IntegerField()),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constructor_id', models.IntegerField()),
                ('constructor_ref', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.IntegerField()),
                ('driver_ref', models.CharField(max_length=255)),
                ('number', models.IntegerField(null=True)),
                ('code', models.CharField(max_length=3)),
                ('forename', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Qualifying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualify_id', models.IntegerField()),
                ('number', models.IntegerField()),
                ('position', models.IntegerField()),
                ('q1', models.CharField(max_length=255)),
                ('q2', models.CharField(max_length=255)),
                ('q3', models.CharField(max_length=255)),
                ('constructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.constructor')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('round', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField(null=True)),
                ('url', models.URLField(max_length=255)),
                ('fp1_date', models.DateField(null=True)),
                ('fp1_time', models.TimeField(null=True)),
                ('fp2_date', models.DateField(null=True)),
                ('fp2_time', models.TimeField(null=True)),
                ('fp3_date', models.DateField(null=True)),
                ('fp3_time', models.TimeField(null=True)),
                ('quali_date', models.DateField(null=True)),
                ('quali_time', models.TimeField(null=True)),
                ('sprint_date', models.DateField(null=True)),
                ('sprint_time', models.TimeField(null=True)),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.circuit')),
                ('constructors', models.ManyToManyField(to='f1data.constructor')),
                ('drivers', models.ManyToManyField(to='f1data.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField()),
                ('number', models.IntegerField()),
                ('grid', models.IntegerField()),
                ('position', models.IntegerField(null=True)),
                ('position_text', models.CharField(max_length=255)),
                ('position_order', models.IntegerField()),
                ('points', models.FloatField()),
                ('laps', models.IntegerField()),
                ('time', models.TimeField(null=True)),
                ('milliseconds', models.IntegerField(null=True)),
                ('fastest_lap', models.IntegerField(null=True)),
                ('rank', models.IntegerField(null=True)),
                ('fastest_lap_time', models.CharField(max_length=255)),
                ('fastest_lap_speed', models.CharField(max_length=255)),
                ('constructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.constructor')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_id', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SprintResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField()),
                ('number', models.IntegerField()),
                ('grid', models.IntegerField()),
                ('position', models.IntegerField(null=True)),
                ('position_text', models.CharField(max_length=255)),
                ('position_order', models.IntegerField()),
                ('points', models.FloatField()),
                ('laps', models.IntegerField()),
                ('time', models.TimeField(null=True)),
                ('milliseconds', models.IntegerField(null=True)),
                ('fastest_lap', models.IntegerField(null=True)),
                ('fastest_lap_time', models.CharField(max_length=255)),
                ('constructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.constructor')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.status')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('url', models.URLField(max_length=255)),
                ('circuits', models.ManyToManyField(to='f1data.circuit')),
                ('constructors', models.ManyToManyField(to='f1data.constructor')),
                ('drivers', models.ManyToManyField(to='f1data.driver')),
                ('qualifying', models.ManyToManyField(to='f1data.qualifying')),
                ('races', models.ManyToManyField(to='f1data.race')),
                ('results', models.ManyToManyField(to='f1data.result')),
                ('sprint_results', models.ManyToManyField(to='f1data.sprintresult')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.status'),
        ),
        migrations.AddField(
            model_name='qualifying',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race'),
        ),
        migrations.CreateModel(
            name='PitStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop', models.IntegerField()),
                ('lap', models.IntegerField()),
                ('time', models.TimeField()),
                ('duration', models.CharField(max_length=255)),
                ('milliseconds', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
            ],
        ),
        migrations.CreateModel(
            name='LapTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lap', models.IntegerField()),
                ('position', models.IntegerField()),
                ('time', models.CharField(max_length=255)),
                ('milliseconds', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
            ],
        ),
        migrations.CreateModel(
            name='DriverStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_standing_id', models.IntegerField()),
                ('points', models.FloatField()),
                ('position', models.IntegerField()),
                ('position_text', models.CharField(max_length=255)),
                ('wins', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
            ],
        ),
        migrations.CreateModel(
            name='ConstructorStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constructor_standings_id', models.IntegerField()),
                ('points', models.FloatField()),
                ('position', models.IntegerField()),
                ('position_text', models.CharField(max_length=255)),
                ('wins', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
            ],
        ),
        migrations.CreateModel(
            name='ConstructorResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constructor_result', models.IntegerField()),
                ('points', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='f1data.race')),
            ],
        ),
    ]