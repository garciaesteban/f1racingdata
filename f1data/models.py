from django.db import models

# Create your models here.
class Season(models.Model):
    year = models.IntegerField()
    url = models.URLField(max_length=255)
    races = models.ManyToManyField('Race')
    qualifying = models.ManyToManyField('Qualifying')
    results = models.ManyToManyField('Result')
    sprintresults = models.ManyToManyField('Sprintresult')
    drivers = models.ManyToManyField('Driver')
    constructors = models.ManyToManyField('Constructor')
    circuits = models.ManyToManyField('Circuit')
