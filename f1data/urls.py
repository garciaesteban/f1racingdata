from django.urls import path
from . import views

app_name = "f1data"
urlpatterns = [
    path('', views.home, name="home"),
    path('season/', views.season, name="season"),
    path('season/<int:year>/', views.detail_season, name="detail_season"),
    path('races/', views.races, name="races"),
    path('races/<int:race>/', views.detail_race, name="detail_race"),
]
