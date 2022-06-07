from django.shortcuts import render
from django.http import HttpResponse
from f1data.models import *

# Create your views here.
def home(request):
    template = "f1data/home/home.html"
    current_season = Season.objects.first()
    last_race = DriverStanding.objects.order_by("race").first().race
    if last_race.round < current_season.races.count():
        next_race = current_season.races.get(round=last_race.round + 1)
    else:
        next_race = None

    results = Result.objects.filter(race=last_race)
    sprint_results = SprintResult.objects.filter(race=last_race)
    qualifying = Qualifying.objects.filter(race=last_race)
    driver_standings = DriverStanding.objects.filter(race=last_race).order_by('position')
    constructor_standings = ConstructorStanding.objects.filter(race=last_race).order_by('position')
    constructor_results = ConstructorResult.objects.filter(race=last_race)

    context = {
        "current_season": current_season,
        "last_race": last_race,
        "next_race": next_race,
        "results": results,
        "sprint_results": sprint_results,
        "qualifying": qualifying,
        "driver_standings": driver_standings,
        "constructor_standings": constructor_standings,
        "constructor_results": constructor_results
    }
    return render(request,template,context)
