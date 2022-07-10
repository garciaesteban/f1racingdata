from django.urls import path
from . import views

app_name = "f1data"
urlpatterns = [
    path('', views.home, name="home"),
    path('season/<int:year>/', views.season, name="season"),
]
