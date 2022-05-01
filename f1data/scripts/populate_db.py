import csv
import os
from django.utils.timezone import *
from .table_classes import *


def run():
    drivers = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/drivers.csv")
    constructors = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/constructors.csv")
    circuits = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/circuits.csv")
    drivers = csv.DictReader(drivers)
    constructors = csv.DictReader(constructors)
    circuits = csv.DictReader(circuits)
    drivers_dict = {}
    constructors_dict = {}
    circuits_dict = {}

    for driver in drivers:
        temp_driver = DriverTable(**driver)
        drivers_dict[temp_driver.driverId] = temp_driver

    for constructor in constructors:
        temp_constructor = ConstructorTable(**constructor)
        constructors_dict[temp_constructor.constructorId] = temp_constructor

    for circuit in circuits:
        temp_circuit = CircuitTable(**circuit)
        circuits_dict[temp_circuit.circuitId] = temp_circuit
