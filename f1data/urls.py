from django.urls import path
from . import views

app_name = "f1data"
urlpatterns = [
    path('', views.home, name="home"),
    path('season/', views.season, name="season"),
    path('season/<int:year>/', views.detail_season, name="detail_season"),
    path('races/', views.races, name="races"),
    path('races/<int:race>/', views.detail_race, name="detail_race"),
    path('drivers/', views.drivers, name="drivers"),
    path('drivers/<int:driver>/', views.detail_driver, name="detail_driver"),
    path('constructors/', views.constructors, name="constructors"),
    path('constructors//<int:constructor>/', views.detail_constructor, name="detail_constructor"),
]
