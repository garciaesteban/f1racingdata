import csv
import os
import pandas as pd
from django.utils.timezone import *
from .table_classes import *
from f1data.models import *
from django.forms.models import model_to_dict

class DataImport:
    path_to_csv = f"{os.getcwd()}/f1data/scripts/f1db_csv/"
    csv_len = 0

    def csv_length(self,file):
        for row in file:
            self.csv_len += 1
        self.csv_len -= 1
        file.seek(0)

    def save_model(self,instance):
        instance.save()

    def check_if_exists(self,model_keys):
        dict_key = list(self.filter)[0]
        self.filter[dict_key] = model_keys.__dict__.get(self.id)
        return self.model.objects.filter(**self.filter).exists()

    def clean_dict(self,data):
        for row in data:
            model = self.model_table(**row)
            model_dict = self.model_table.__dict__[self.model_dict]
            model = self.model(**model_dict(model))
            #print(model_to_dict(model))
            print(self.check_if_exists(model))
            if not self.check_if_exists(model):
                self.save_model(model)

    def import_data(self):
        file = open(f"{self.path_to_csv}{self.name}.csv")
        self.csv_length(file)
        data_dict = csv.DictReader(file)
        #self.clean_dict(data_dict)
        if self.csv_len == self.model.objects.count():
            print(f'No Updates To {self.name}\nDB Size: {self.model.objects.count()} CSV Size:{self.csv_len}')
        else:
            self.clean_dict(data_dict)
        file.close()

class DriverImport(DataImport):
    name = "drivers"
    model = Driver
    model_table = DriverTable
    id = 'driver_id'
    model_dict = 'driver_model_dict'
    filter = {'driver_id': None}

class ConstructorImport(DataImport):
    name = 'constructors'
    model = Constructor
    model_table = ConstructorTable
    id = 'constructor_id'
    model_dict = 'constructor_model_dict'
    filter = {'constructor_id': None}

class CircuitImport(DataImport):
    name = "circuits"
    model = Circuit
    model_table = CircuitTable
    id = 'circuit_id'
    model_dict = 'circuit_model_dict'
    filter = {'circuit_id': None}

class StatusImport(DataImport):
    name = 'status'
    model = Status
    model_table = StatusTable
    id = 'status_id'
    model_dict = 'status_model_dict'
    filter = {'status_id': None}

class SeasonImport(DataImport):
    name = 'seasons'
    model = Season
    model_table = SeasonTable
    id = 'year'
    model_dict = 'season_model_dict'
    filter = {'year': None}

class RaceDataImport(DataImport):
    def save_model(self,instance):
        instance.save()
        instance = self.model.objects.get(race_id=instance.race_id)

        season = Season.objects.get(year=instance.year)
        circuit = Circuit.objects.get(circuit_id=instance.circuit.circuit_id)

        if not season.races.filter(race_id=instance.race_id).exists():
            season.races.add(instance)

        if not season.circuits.filter(
            circuit_id=instance.circuit.circuit_id
        ).exists():
            season.circuits.add(circuit)

class RaceImport(RaceDataImport):
    name = 'races'
    model = Race
    model_table = RaceTable
    id = 'race_id'
    model_dict = 'race_model_dict'
    filter = {'race_id': None}

class QualifyingDataImport(DataImport):
    def save_model(self,instance):
        instance.save()
        instance = self.model.objects.get(qualify_id=instance.qualify_id)

        year = Race.objects.get(race_id=instance.race.race_id).year
        season = Season.objects.get(year=year)

        if not season.qualifying.filter(qualify_id=instance.qualify_id).exists():
            season.qualifying.add(instance)

class QualifyingImport(QualifyingDataImport):
    name = 'qualifying'
    model = Qualifying
    model_table = QualifyingTable
    id = 'qualify_id'
    model_dict = 'qualifying_model_dict'
    filter = {'qualify_id': None}

class SprintResultDataImport(DataImport):
    def save_model(self,instance):
        instance.save()
        instance = self.model.objects.get(result_id=instance.result_id)

        year = Race.objects.get(race_id=instance.race.race_id).year
        season = Season.objects.get(year=year)

        if not season.sprint_results.filter(result_id=instance.result_id).exists():
            season.sprint_results.add(instance)

class SprintResultImport(SprintResultDataImport):
    name = 'sprint_results'
    model = SprintResult
    model_table = SprintResultTable
    id = 'result_id'
    model_dict = 'sprint_result_model_dict'
    filter = {'result_id': None}

class ResultDataImport(DataImport):
    def save_model(self,instance):
        instance.save()
        instance = self.model.objects.get(result_id=instance.result_id)

        race = Race.objects.get(race_id=instance.race.race_id)
        season = Season.objects.get(year=race.year)
        driver = Driver.objects.get(driver_id=instance.driver.driver_id)
        constructor = Constructor.objects.get(constructor_id=instance.constructor.constructor_id)

        if not season.results.filter(result_id=instance.result_id).exists():
            season.results.add(instance)

        if not season.drivers.filter(driver_id=driver.driver_id).exists():
            season.drivers.add(driver)

        if not season.constructors.filter(constructor_id=constructor.constructor_id).exists():
            season.constructors.add(constructor)

        if not race.drivers.filter(driver_id=driver.driver_id).exists():
            race.drivers.add(driver)

        if not race.constructors.filter(constructor_id=constructor.constructor_id):
            race.constructors.add(constructor)

class ResultImport(ResultDataImport):
    name = 'results'
    model = Result
    model_table = ResultTable
    id = 'result_id'
    model_dict = 'result_model_dict'
    filter = {'result_id': None}

class DriverStandingImport(DataImport):
    name  = 'driver_standings'
    model = DriverStanding
    model_table = DriverStandingTable
    id = 'driver_standing_id'
    model_dict = 'driver_standing_model_dict'
    filter = {'driver_standing_id': None}

class ConstructorStandingImport(DataImport):
    name = 'constructor_standings'
    model = ConstructorStanding
    model_table = ConstructorStandingTable
    id = 'constructor_standings_id'
    model_dict = 'constructor_standing_model_dict'
    filter = {'constructor_standings_id': None}

class ConstructorResultImport(DataImport):
    name = 'constructor_results'
    model = ConstructorResult
    model_table = ConstructorResultTable
    id = 'constructor_result_id'
    model_dict = 'constructor_result_model_dict'
    filter = {'constructor_result_id': None}

def run():
    drivers = DriverImport()
    drivers.import_data()
    constructors = ConstructorImport()
    constructors.import_data()
    circuits = CircuitImport()
    circuits.import_data()
    status = StatusImport()
    status.import_data()
    seasons = SeasonImport()
    seasons.import_data()
    races = RaceImport()
    races.import_data()
    qualifying = QualifyingImport()
    qualifying.import_data()
    sprintresults = SprintResultImport()
    sprintresults.import_data()
    results = ResultImport()
    results.import_data()
    driver_standings = DriverStandingImport()
    driver_standings.import_data()
    constructor_standings = ConstructorStandingImport()
    constructor_standings.import_data()
    constructor_results = ConstructorResultImport()
    constructor_results.import_data()
