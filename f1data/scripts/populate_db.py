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

    for driver in drivers:
        temp_driver = DriverTable(**driver)
        create_driver = Driver(**temp_driver.driver_model_dict())
        if not Driver.objects.filter(driver_id=create_driver.driver_id).exists():
            create_driver.save()

    for constructor in constructors:
        temp_constructor = ConstructorTable(**constructor)
        create_constructor = Constructor(**temp_constructor.constructor_model_dict())
        if not Constructor.objects.filter(
            constructor_id=create_constructor.constructor_id
        ).exists():
            create_constructor.save()

    for circuit in circuits:
        temp_circuit = CircuitTable(**circuit)
        create_circuit = Circuit(**temp_circuit.circuit_model_dict())
        if not Circuit.objects.filter(circuit_id=create_circuit.circuit_id).exists():
            create_circuit.save()

    for stat in status:
        temp_stat = StatusTable(**stat)
        create_stat = Status(**temp_stat.status_model_dict())
        if not Status.objects.filter(status_id=create_stat.status_id).exists():
            create_stat.save()

    for season in seasons:
        temp_season = SeasonTable(**season)
        create_season = Season(**temp_season.season_model_dict())
        if not Season.objects.filter(year=create_season.year).exists():
            create_season.save()

    for race in races:
        temp_race = RaceTable(**race)
        create_race = Race(**temp_race.race_model_dict())
        if not Race.objects.filter(race_id=create_race.race_id).exists():
            create_race.save()

        create_race = Race.objects.get(race_id=create_race.race_id)
        temp_season = Season.objects.get(year=create_race.year)
        temp_circuit = Circuit.objects.get(circuit_id=create_race.circuit.circuit_id)

        if not temp_season.races.filter(race_id=create_race.race_id).exists():
            temp_season.races.add(create_race)

        if not temp_season.circuits.filter(
            circuit_id=create_race.circuit.circuit_id
        ).exists():
            temp_season.circuits.add(temp_circuit)

    for quali in qualifying:
        temp_qualifying = QualifyingTable(**quali)
        create_qualifying = Qualifying(**temp_qualifying.qualifying_model_dict())

        if not Qualifying.objects.filter(
            qualify_id=create_qualifying.qualify_id
        ).exists():
            create_qualifying.save()

        create_qualifying = Qualifying.objects.get(
            qualify_id=create_qualifying.qualify_id
        )
        temp_year = Race.objects.get(race_id=create_qualifying.race.race_id).year
        temp_season = Season.objects.get(year=temp_year)
        if not temp_season.qualifying.filter(
            qualify_id=create_qualifying.qualify_id
        ).exists():
            temp_season.qualifying.add(create_qualifying)

    for sprint in sprint_results:
        temp_sprint = SprintResultTable(**sprint)
        create_sprint_result = SprintResult(**temp_sprint.sprint_result_model_dict())

        if not SprintResult.objects.filter(result_id=create_sprint_result.result_id):
            create_sprint_result.save()

        create_sprint_result = SprintResult.objects.get(
            result_id=create_sprint_result.result_id
        )
        temp_year = Race.objects.get(race_id=create_sprint_result.race.race_id).year
        temp_season = Season.objects.get(year=temp_year)
        if not temp_season.sprint_results.filter(
            race_id=create_sprint_result.result_id
        ).exists():
            temp_season.sprint_results.add(create_sprint_result)

    for result in results:
        temp_result = ResultTable(**result)
        create_result = Result(**temp_result.result_model_dict())
        if not Result.objects.filter(result_id=create_result.result_id):
            create_result.save()

        create_result = Result.objects.get(result_id=create_result.result_id)
        temp_race = Race.objects.get(race_id=create_result.race.race_id)
        temp_season = Season.objects.get(year=temp_race.year)
        temp_driver = Driver.objects.get(driver_id=create_result.driver.driver_id)
        temp_constructor = Constructor.objects.get(
            constructor_id=create_result.constructor.constructor_id
        )
        if not temp_season.results.filter(result_id=create_result.result_id).exists():
            temp_season.results.add(create_result)

        if not temp_season.drivers.filter(driver_id=temp_driver.driver_id).exists():
            temp_season.drivers.add(temp_driver)

        if not temp_season.constructors.filter(
            constructor_id=temp_constructor.constructor_id
        ).exists():
            temp_season.constructors.add(temp_constructor)

        if not temp_race.drivers.filter(driver_id=temp_driver.driver_id).exists():
            temp_race.drivers.add(temp_driver)

        if not temp_race.constructors.filter(
            constructor_id=temp_constructor.constructor_id
        ).exists():
            temp_race.constructors.add(temp_constructor)

    for pit_stop in pit_stops:
        temp_pit_stop = PitStopTable(**pit_stop)
        create_pit_stop = PitStop(**temp_pit_stop.pit_stops_model_dict())

        if not PitStop.objects.filter(
            race=create_pit_stop.race,
            driver=create_pit_stop.driver,
            stop=create_pit_stop.stop,
        ).exists():
            create_pit_stop.save()

    for lap_time in lap_times:
        temp_lap_time = LapTimeTable(**lap_time)
        create_lap_time = LapTime(**temp_lap_time.lap_time_model_dict())

        if not LapTime.objects.filter(
            race=create_lap_time.race,
            driver=create_lap_time.driver,
            lap=create_lap_time.lap,
        ).exists():
            create_lap_time.save()

    for driver_standing in driver_standings:
        temp_driver_standing = DriverStandingTable(**driver_standing)
        create_driver_standing = DriverStanding(
            **temp_driver_standing.driver_standing_model_dict()
        )

        if not DriverStanding.objects.filter(
            driver_standing_id=create_driver_standing.driver_standing_id
        ).exists():
            create_driver_standing.save()

    for constructor_standing in constructor_standings:
        temp_constructor_standing = ConstructorStandingTable(**constructor_standing)
        create_constructor_standing = ConstructorStanding(
            **temp_constructor_standing.constructor_standing_model_dict()
        )

        if not ConstructorStanding.objects.filter(
            constructor_standings_id=create_constructor_standing.constructor_standings_id
        ).exists():
            create_constructor_standing.save()

    for constructor_result in constructor_results:
        temp_constructor_result = ConstructorResultTable(**constructor_result)
        create_constructor_result = ConstructorResult(
            **temp_constructor_result.constructor_result_model_dict()
        )

        if not ConstructorResult.objects.filter(
            constructor_result_id=create_constructor_result.constructor_result_id
        ).exists():
            create_constructor_result.save()
