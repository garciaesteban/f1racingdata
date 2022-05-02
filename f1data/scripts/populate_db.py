import csv
import os
from django.utils.timezone import *
from .table_classes import *


def run():
    drivers = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/drivers.csv")
    constructors = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/constructors.csv")
    circuits = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/circuits.csv")
    seasons = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/seasons.csv")
    races = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/races.csv")
    drivers = csv.DictReader(drivers)
    constructors = csv.DictReader(constructors)
    circuits = csv.DictReader(circuits)
    seasons = csv.DictReader(seasons)
    races = csv.DictReader(races)
    drivers_dict = {}
    constructors_dict = {}
    circuits_dict = {}
    seasons_dict = {}
    races_dict = {}

    for driver in drivers:
        temp_driver = DriverTable(**driver)
        drivers_dict[temp_driver.driverId] = temp_driver

    for constructor in constructors:
        temp_constructor = ConstructorTable(**constructor)
        constructors_dict[temp_constructor.constructorId] = temp_constructor

    for circuit in circuits:
        temp_circuit = CircuitTable(**circuit)
        circuits_dict[temp_circuit.circuitId] = temp_circuit

    for season in seasons:
        temp_season = SeasonTable(**season)
        seasons_dict[temp_season.year] = temp_season

    for race in races:
        temp_race = RaceTable(**race)
        print(f"{temp_race.time}")
