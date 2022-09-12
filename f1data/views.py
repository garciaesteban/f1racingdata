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

class DriversRedirectView(RedirectView):
    year = Season.objects.first().year
    url = f'{year}/'

class Drivers(ListView):
    template_name = "f1data/drivers/drivers.html"
    context_object_name = 'drivers'

    def get_queryset(self,*kwargs):
        year = self.__dict__['kwargs']['year']
        return Season.objects.get(year=year).drivers.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        seasons = Season.objects.values('year')
        context['seasons'] = seasons
        context['year'] = self.__dict__['kwargs']['year']
        return context

def detail_driver(request,driver):
    return HttpResponse("Detail Driver")

class ConstructorsRedirectView(RedirectView):
    year = Season.objects.first().year
    url = f'{year}'

class Constructors(ListView):
    template_name = "f1data/constructors/constructors.html"
    context_object_name = 'constructors'

    def get_queryset(self,**kwargs):
        year = self.__dict__['kwargs']['year']
        return Season.objects.get(year=year).constructors.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        seasons = Season.objects.values('year')
        context['seasons'] = seasons
        context['year'] = self.__dict__['kwargs']['year']
        return context

def detail_constructor(request,constructor):
    return HttpResponse("Detail Constructor")

class DriverStandingsRedirectView(RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        year = Season.objects.first().year
        round = DriverStanding.objects.order_by("race").first().race.round
        return f"{year}/"

class DriverStandings(ListView):
    template_name = "f1data/driver_standings/driver_standings.html"
    context_object_name = 'driver_standings'

    def get_queryset(self,**kwargs):
        year = self.kwargs['year']
        races = Race.objects.filter(year=year)
        driver_standings = []
        for race in races:
            query_set = DriverStanding.objects.filter(race=race).order_by('position')
            if query_set.exists():
                driver_standings.append(query_set)
        return driver_standings

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        rounds = []
        season = self.kwargs['year']
        context['current_season'] = Season.objects.get(year=season)
        context['seasons'] = Season.objects.values('year')
        races = Race.objects.filter(year=season).order_by('round')

        for race in races:
            if DriverStanding.objects.filter(race=race).exists():
                rounds.append(race)

        context['races'] = rounds
        return context
