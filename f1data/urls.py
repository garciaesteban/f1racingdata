from django.urls import path
from . import views

app_name = "f1data"
urlpatterns = [
    path('', views.home, name="home"),
    path('season/<int:page>/', views.Seasons.as_view(),name="seasons"),
    path('season/<int:year>/', views.detail_season, name="detail_season"),
    path('races/', views.RacesRedirectView.as_view(), name="races"),
    path('races/<int:year>/', views.Races.as_view(), name="races"),
    path('races/<int:race>/', views.detail_race, name="detail_race"),
    path('drivers/<int:year>/', views.Drivers.as_view(), name="drivers"),
    path('drivers/', views.DriversRedirectView.as_view(), name="drivers"),
    path('drivers/<int:driver>/', views.detail_driver, name="detail_driver"),
    path('constructors/', views.ConstructorsRedirectView.as_view(), name="constructors"),
    path('constructors/<int:year>/', views.Constructors.as_view(), name="constructors"),
    path('constructors/<int:constructor>/', views.detail_constructor, name="detail_constructor"),
    path('driver_standings/<int:year>/', views.DriverStandings.as_view(), name="driver_standings"),
    path('driver_standings/', views.DriverStandingsRedirectView.as_view(), name="driver_standings"),
    path('constructors_standings/<int:year>/', views.ConstructorStandings.as_view(), name="constructors_standings"),
    path('constructors_standings/', views.ConstructorStandingsRedirectView.as_view(), name="constructors_standings"),
]
