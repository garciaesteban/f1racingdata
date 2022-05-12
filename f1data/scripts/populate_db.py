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
    qualifying = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/qualifying.csv")
    sprint_results = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/sprint_results.csv")
    status = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/status.csv")
    results = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/results.csv")
    drivers = csv.DictReader(drivers)
    constructors = csv.DictReader(constructors)
    circuits = csv.DictReader(circuits)
    seasons = csv.DictReader(seasons)
    races = csv.DictReader(races)
    qualifying = csv.DictReader(qualifying)
    sprint_results = csv.DictReader(sprint_results)
    status = csv.DictReader(status)
    results = csv.DictReader(results)

    drivers_dict = {}
    constructors_dict = {}
    circuits_dict = {}
    seasons_dict = {}
    races_dict = {}
    qualifying_dict = {}
    sprint_results_dict = {}
    status_dict = {}
    results_dict = {}

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
        races_dict[temp_race.raceId] = temp_race

    for quali in qualifying:
        temp_qualifying = QualifyingTable(**quali)
        qualifying_dict[temp_qualifying.qualifyId] = temp_qualifying

    for sprint in sprint_results:
        temp_sprint = SprintResultTable(**sprint)
        sprint_results_dict[temp_sprint.resultId] = temp_sprint

    for stat in status:
        temp_stat = StatusTable(**stat)
        status_dict[temp_stat] = temp_stat

    for result in results:
        temp_result = ResultTable(**result)
        results_dict[temp_result.resultId] = temp_result
