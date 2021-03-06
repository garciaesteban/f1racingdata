from django.db import models

# Create your models here.
class Season(models.Model):
    year = models.IntegerField()
    url = models.URLField(max_length=255)
    races = models.ManyToManyField('Race')
    qualifying = models.ManyToManyField('Qualifying')
    results = models.ManyToManyField('Result')
    sprint_results = models.ManyToManyField('SprintResult')
    drivers = models.ManyToManyField('Driver')
    constructors = models.ManyToManyField('Constructor')
    circuits = models.ManyToManyField('Circuit')

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.year}"

class Race(models.Model):
    race_id = models.IntegerField()
    year = models.IntegerField()
    round = models.IntegerField()
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(null=True)
    url = models.URLField(max_length=255)
    fp1_date = models.DateField(null=True)
    fp1_time = models.TimeField(null=True)
    fp2_date = models.DateField(null=True)
    fp2_time = models.TimeField(null=True)
    fp3_date = models.DateField(null=True)
    fp3_time = models.TimeField(null=True)
    quali_date = models.DateField(null=True)
    quali_time = models.TimeField(null=True)
    sprint_date = models.DateField(null=True)
    sprint_time = models.TimeField(null=True)
    drivers = models.ManyToManyField('Driver')
    constructors = models.ManyToManyField('Constructor')
    circuit = models.ForeignKey('Circuit',on_delete=models.PROTECT)

    class Meta:
        ordering = ['-year','-round']

    def __str__(self):
        return f"{self.year} {self.round} {self.circuit}"

class Qualifying(models.Model):
    qualify_id = models.IntegerField()
    number = models.IntegerField()
    position = models.IntegerField()
    q1 = models.CharField(max_length=255)
    q2 = models.CharField(max_length=255)
    q3 = models.CharField(max_length=255)
    driver = models.ForeignKey('Driver',on_delete=models.PROTECT)
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    constructor = models.ForeignKey('Constructor',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.position} {self.driver} {self.race} {self.constructor}"

class Result(models.Model):
    result_id = models.IntegerField()
    number = models.IntegerField(null=True)
    grid = models.IntegerField()
    position = models.IntegerField(null=True)
    position_text = models.CharField(max_length=255)
    position_order = models.IntegerField()
    points = models.FloatField()
    laps = models.IntegerField()
    time = models.CharField(max_length=255,default="")
    milliseconds = models.IntegerField(null=True)
    fastest_lap = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    fastest_lap_time = models.CharField(max_length=255)
    fastest_lap_speed = models.CharField(max_length=255)
    status = models.ForeignKey('Status',on_delete=models.PROTECT)
    driver = models.ForeignKey('Driver',on_delete=models.PROTECT)
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    constructor = models.ForeignKey('Constructor',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.driver} {self.race} {self.constructor}"

class SprintResult(models.Model):
    result_id = models.IntegerField()
    number = models.IntegerField()
    grid = models.IntegerField()
    position = models.IntegerField(null=True)
    position_text = models.CharField(max_length=255)
    position_order = models.IntegerField()
    points = models.FloatField()
    laps = models.IntegerField()
    time = models.CharField(max_length=255,default="")
    milliseconds = models.IntegerField(null=True)
    fastest_lap = models.IntegerField(null=True)
    fastest_lap_time = models.CharField(max_length=255)
    status = models.ForeignKey('Status',on_delete=models.PROTECT)
    driver = models.ForeignKey('Driver',on_delete=models.PROTECT)
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    constructor = models.ForeignKey('Constructor',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.driver} {self.race} {self.constructor}"

class Driver(models.Model):
    driver_id = models.IntegerField()
    driver_ref = models.CharField(max_length=255)
    number = models.IntegerField(null=True)
    code = models.CharField(max_length=3)
    forename = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.surname} {self.forename} {self.code} {self.number}"

class Constructor(models.Model):
    constructor_id = models.IntegerField()
    constructor_ref = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.constructor_id} {self.name}"

class Circuit(models.Model):
    circuit_id = models.IntegerField()
    circuit_ref = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    alt = models.IntegerField(null=True)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Status(models.Model):
    status_id = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.status_id} {self.status}"

class PitStop(models.Model):
    stop = models.IntegerField()
    lap = models.IntegerField()
    time = models.TimeField()
    duration = models.CharField(max_length=255)
    milliseconds = models.IntegerField()
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    driver = models.ForeignKey('Driver',on_delete=models.PROTECT)

class LapTime(models.Model):
    lap = models.IntegerField()
    position = models.IntegerField()
    time = models.CharField(max_length=255)
    milliseconds = models.IntegerField()
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    driver = models.ForeignKey('Driver',on_delete=models.PROTECT)

class DriverStanding(models.Model):
    driver_standing_id = models.IntegerField()
    points = models.FloatField()
    position = models.IntegerField()
    position_text = models.CharField(max_length=255)
    wins = models.IntegerField()
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    driver = models.ForeignKey('Driver',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.driver} {self.race}"

class ConstructorStanding(models.Model):
    constructor_standings_id = models.IntegerField()
    points = models.FloatField()
    position = models.IntegerField()
    position_text = models.CharField(max_length=255)
    wins = models.IntegerField()
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    constructor = models.ForeignKey('Constructor',on_delete=models.PROTECT,default=None)

class ConstructorResult(models.Model):
    constructor_result_id = models.IntegerField()
    points = models.FloatField()
    status = models.CharField(max_length=255)
    race = models.ForeignKey('Race',on_delete=models.PROTECT)
    constructor = models.ForeignKey('Constructor',on_delete=models.PROTECT,default=None)
