from datetime import datetime


class DriverTable:
    def __init__(
        self,
        driverId,
        driverRef,
        number,
        code,
        forename,
        surname,
        dob,
        nationality,
        url,
    ):
        self.driverId = driverId
        self.driverRef = driverRef
        self.forename = forename
        self.surname = surname
        self.nationality = nationality
        self.url = url

        dob = datetime.strptime(dob, "%Y-%m-%d")
        self.dob = dob.date()
        if number != "\\N":
            self.number = number
        else:
            self.number = None
        if code != "\\N":
            self.code = code
        else:
            self.code = ""

    def __str__(self):
        return f"{self.driverId} {self.driverRef} {self.number} {self.code} {self.forename} {self.surname} {self.dob} {self.nationality}"
