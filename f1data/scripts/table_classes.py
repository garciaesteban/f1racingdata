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


class ConstructorTable:
    def __init__(self, constructorId, constructorRef, name, nationality, url):
        self.constructorId = constructorId
        self.constructorRef = constructorRef
        self.name = name
        self.nationality = nationality
        self.url = url

    def __str__(self):
        return f"{self.constructorId} {self.constructorRef} {self.name} {self.nationality} {self.url}"
