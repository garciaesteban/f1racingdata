from django import template
from f1data.models import Result, Season, DriverStanding, ConstructorStanding

register = template.Library()

@register.filter(name='driver')
def driver(value):
    last_race_standings = DriverStanding.objects.filter(race__year=value).order_by('-points').first()
    driver = last_race_standings.driver
    return f"{driver.forename} {driver.surname}"

@register.filter(name='constructor')
def constructor(value):
    last_race_constructors_standings = ConstructorStanding.objects.filter(race__year=value).order_by('-points').first()
    if last_race_constructors_standings != None:
        return last_race_constructors_standings.constructor.name
    else:
        return 'No Constructor'
    #constructor = last_race_constructors_standings.constructor
    #print(f"{constructor} {value}")
