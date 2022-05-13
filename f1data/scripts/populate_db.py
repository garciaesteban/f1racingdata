import csv
import os
from django.utils.timezone import *
from .table_classes import *
from f1data.models import *


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
    pit_stops = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/pit_stops.csv")
    lap_times = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/lap_times.csv")
    driver_standings = open(
        f"{os.getcwd()}/f1data/scripts/f1db_csv/driver_standings.csv"
    )
    constructor_standings = open(
        f"{os.getcwd()}/f1data/scripts/f1db_csv/constructor_standings.csv"
    )
    constructor_results = open(
        f"{os.getcwd()}/f1data/scripts/f1db_csv/constructor_results.csv"
    )
    drivers = csv.DictReader(drivers)
    constructors = csv.DictReader(constructors)
    circuits = csv.DictReader(circuits)
    seasons = csv.DictReader(seasons)
    races = csv.DictReader(races)
    qualifying = csv.DictReader(qualifying)
    sprint_results = csv.DictReader(sprint_results)
    status = csv.DictReader(status)
    results = csv.DictReader(results)
    pit_stops = csv.DictReader(pit_stops)
    lap_times = csv.DictReader(lap_times)
    driver_standings = csv.DictReader(driver_standings)
    constructor_standings = csv.DictReader(constructor_standings)
    constructor_results = csv.DictReader(constructor_results)

    drivers_dict = {}
    constructors_dict = {}
    circuits_dict = {}
    seasons_dict = {}
    races_dict = {}
    qualifying_dict = {}
    sprint_results_dict = {}
    status_dict = {}
    results_dict = {}
    pit_stops_dict = {}
    lap_times_dict = {}
    driver_standings_dict = {}
    constructor_standings_dict = {}
    constructor_results_dict = {}

    for driver in drivers:
        temp_driver = DriverTable(**driver)
        drivers_dict[temp_driver.driverId] = temp_driver
        create_driver = Driver(**temp_driver.driver_model_dict())
        create_driver.save()

    for constructor in constructors:
        temp_constructor = ConstructorTable(**constructor)
        constructors_dict[temp_constructor.constructorId] = temp_constructor

    for circuit in circuits:
        temp_circuit = CircuitTable(**circuit)
        circuits_dict[temp_circuit.circuitId] = temp_circuit

    for stat in status:
        temp_stat = StatusTable(**stat)
        status_dict[temp_stat] = temp_stat

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

    for result in results:
        temp_result = ResultTable(**result)
        results_dict[temp_result.resultId] = temp_result

    for pit_stop in pit_stops:
        temp_pit_stop = PitStopTable(**pit_stop)
        results_dict[temp_pit_stop.raceId] = temp_pit_stop

    for lap_time in lap_times:
        temp_lap_time = LapTimeTable(**lap_time)
        lap_times_dict[temp_lap_time.raceId] = temp_lap_time

    for driver_standing in driver_standings:
        temp_driver_standing = DriverStandingTable(**driver_standing)
        driver_standings_dict[
            temp_driver_standing.driverStandingsId
        ] = temp_driver_standing

    for constructor_standing in constructor_standings:
        temp_constructor_standing = ConstructorStandingTable(**constructor_standing)
        constructor_standings_dict[
            temp_constructor_standing.constructorStandingsId
        ] = temp_constructor_standing

    for constructor_result in constructor_results:
        temp_constructor_result = ConstructorResultTable(**constructor_result)
        constructor_results_dict[
            temp_constructor_result.constructorResultsId
        ] = temp_constructor_result
