import csv
import os
from django.utils.timezone import *
from .table_classes import *


def run():
    drivers = open(f"{os.getcwd()}/f1data/scripts/f1db_csv/drivers.csv")
    drivers = csv.DictReader(drivers)
    drivers_dict = {}

    for driver in drivers:
        temp_driver = DriverTable(**driver)
        drivers_dict[temp_driver.driverId] = temp_driver
