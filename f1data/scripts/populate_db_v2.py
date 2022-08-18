import csv
import os
import pandas as pd
from django.utils.timezone import *
from .table_classes import *
from f1data.models import *

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

    def clean_dict(self,data):
        for row in data:
            temp_model = self.model_table(**row)
            temp_model = self.model(**self.model_dict(temp_model))
            temp = temp_model.__dict__.get(self.id)
            if not self.check_if_exists(temp):
                self.save_model(temp_model)

    def import_data(self):
        file = open(f"{self.path_to_csv}{self.name}.csv")
        self.csv_length(file)
        data_dict = csv.DictReader(file)
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

    def model_dict(self,driver_data):
        return driver_data.driver_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(driver_id=key).exists()

class ConstructorImport(DataImport):
    name = 'constructors'
    model = Constructor
    model_table = ConstructorTable
    id = 'constructor_id'

    def model_dict(self,constructor_data):
        return constructor_data.constructor_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(constructor_id=key).exists()

class CircuitImport(DataImport):
    name = 'circuits'
    model = Circuit
    model_table = CircuitTable
    id = 'circuit_id'

    def model_dict(self,circuit_data):
        return circuit_data.circuit_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(circuit_id=key).exists()

class StatusImport(DataImport):
    name = 'status'
    model = Status
    model_table = StatusTable
    id = 'status_id'

    def model_dict(self,status_data):
        return status_data.status_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(status_id=key).exists()

class SeasonImport(DataImport):
    name = 'seasons'
    model = Season
    model_table = SeasonTable
    id = 'year'

    def model_dict(self,season_data):
        return season_data.season_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(year=key).exists()

class RaceDataImport(DataImport):

    def save_model(self,instance):
        instance.save()
        instance = model.objects.get(race_id=instance.race_id)

        temp_season = Season.objects.get(year=instance.year)
        temp_circuit = Circuit.objects.get(circuit_id=instace.circuit.circuit_id)

        if not temp_season.races.filter(race_id=create_race.race_id).exists():
            temp_season.races.add(create_race)

        if not temp_season.circuits.filter(
            circuit_id=create_race.circuit.circuit_id
        ).exists():
            temp_season.circuits.add(temp_circuit)

class RaceImport(RaceDataImport):
    name = 'races'
    model = Race
    model_table = RaceTable
    id = 'race_id'

    def model_dict(self,race_data):
        return race_data.race_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(race_id=key).exists()

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

    def model_dict(self,qualifying_data):
        return qualifying_data.qualifying_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(qualify_id=key).exists()

class SprintResultDataImport(DataImport):
    def save_model(self,instance):
        instance.save()
        instance = self.model.objects.get(result_id=instance.result_id)

class SprintResultImport(SprintResultDataImport):
    name = 'sprint_results'
    model = SprintResult
    model_table = SprintResultTable
    id = 'result_id'

    def model_dict(self,sprint_result_data):
        return sprint_result_data.sprint_result_model_dict()

    def check_if_exists(self,key):
        return self.model.objects.filter(result_id=key).exists()


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
    sprint_results = SprintResultImport()
