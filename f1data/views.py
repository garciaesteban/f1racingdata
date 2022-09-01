from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.base import RedirectView
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

class Seasons(ListView):
    model = Season
    context_object_name = 'seasons'
    paginate_by = 12
    template_name = "f1data/season/season.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context['page_obj']
        if page_obj.number > 2 and (page_obj.paginator.num_pages - page_obj.number) > 2:
            pages = range(page_obj.number-2,page_obj.number+3)
        elif page_obj.number <= 2:
            pages = range(1,5)
        elif (page_obj.paginator.num_pages - page_obj.number) <=2:
            pages = range(page_obj.paginator.num_pages-5,page_obj.paginator.num_pages+1)
        context['pages'] = pages
        return context

def detail_season(request,year):
    return HttpResponse("Detail Season")

class RacesRedirectView(RedirectView):
    year = Season.objects.first().year
    url = f'{year}/'

class Races(ListView):
    template_name = 'f1data/races/races.html'
    context_object_name = 'races'

    def get_queryset(self,**kwargs):
        year = self.__dict__['kwargs']['year']
        return Race.objects.filter(year=year)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        seasons = Season.objects.values('year')
        context['seasons'] = seasons
        context['year'] = self.__dict__['kwargs']['year']
        return context

def detail_race(request,race):
    return HttpResponse("Detail Race")

def drivers(request):
    template = "f1data/drivers/drivers.html"
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers,
    }
    return render(request,template,context)

def detail_driver(request,driver):
    return HttpResponse("Detail Driver")

def constructors(request):
    template = "f1data/constructors/constructors.html"
    constructors = Constructor.objects.all()
    context = {
        'constructors': constructors,
    }

    return render(request,template,context)

def detail_constructor(request,constructor):
    return HttpResponse("Detail Constructor")
