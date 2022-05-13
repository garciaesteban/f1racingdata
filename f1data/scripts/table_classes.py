from datetime import datetime
from django.utils.timezone import make_aware, utc


def format_date(date):
    temp_date = datetime.strptime(date, "%Y-%m-%d")
    return temp_date.date()


def format_time(time):
    if time != "\\N":
        temp_time = datetime.strptime(time, "%H:%M:%S").time()
        temp_time = temp_time.replace(tzinfo=utc)
    else:
        temp_time = None
    return temp_time


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

        dob = format_date(dob)
        self.dob = dob
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

    def driver_model_dict(self):
        return {
            "driver_id": self.driverId,
            "driver_ref": self.driverRef,
            "number": self.number,
            "code": self.code,
            "forename": self.forename,
            "surname": self.surname,
            "dob": self.dob,
            "nationality": self.nationality,
            "url": self.url,
        }


class ConstructorTable:
    def __init__(self, constructorId, constructorRef, name, nationality, url):
        self.constructorId = constructorId
        self.constructorRef = constructorRef
        self.name = name
        self.nationality = nationality
        self.url = url

    def __str__(self):
        return f"{self.constructorId} {self.constructorRef} {self.name} {self.nationality} {self.url}"

    def constructor_model_dict(self):
        return {
            "constructor_id": self.constructorId,
            "constructor_ref": self.constructorRef,
            "name": self.name,
            "nationality": self.nationality,
            "url": self.url,
        }


class CircuitTable:
    def __init__(
        self, circuitId, circuitRef, name, location, country, lat, lng, alt, url
    ):
        self.circuitId = circuitId
        self.circuitRef = circuitRef
        self.name = name
        self.location = location
        self.country = country
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.url = url

    def __str__(self):
        return f"{self.circuitId} {self.circuitRef} {self.name} {self.location}"

    def circuit_model_dict(self):
        return {
            "circuit_id": self.circuitId,
            "circuit_ref": self.circuitRef,
            "name": self.name,
            "location": self.location,
            "country": self.country,
            "lat": self.lat,
            "lng": self.lng,
            "alt": self.alt,
            "url": self.url,
        }


class SeasonTable:
    def __init__(self, year, url):
        self.year = year
        self.url = url

    def __str__(self):
        return f"{self.year} {self.url}"

    def season_model_dict(self):
        return {"year": self.year, "url": self.url}


class RaceTable:
    def __init__(
        self,
        raceId,
        year,
        round,
        circuitId,
        name,
        date,
        time,
        url,
        fp1_date,
        fp1_time,
        fp2_date,
        fp2_time,
        fp3_date,
        fp3_time,
        quali_date,
        quali_time,
        sprint_date,
        sprint_time,
    ):
        self.raceId = raceId
        self.year = year
        self.round = round
        self.circuitId = circuitId
        self.name = name
        self.date = date
        self.url = url

        if time != "\\N":
            time = format_time(time)
            self.time = time
        else:
            self.time = None

        if fp1_date != "\\N":
            temp_date = format_date(fp1_date)
            temp_time = format_time(fp1_time)
            self.fp1_date = temp_date
            self.fp1_time = temp_time
        else:
            self.fp1_date = None
            self.fp1_time = None

        if fp2_date != "\\N":
            temp_date = format_date(fp2_date)
            temp_time = format_time(fp2_time)
            self.fp2_date = temp_date
            self.fp2_time = temp_time
        else:
            self.fp2_date = None
            self.fp2_time = None

        if fp3_date != "\\N":
            temp_date = format_date(fp3_date)
            temp_time = format_time(fp3_time)
            self.fp3_date = temp_date
            self.fp3_time = temp_time
        else:
            self.fp3_date = None
            self.fp3_time = None
        if quali_date != "\\N":
            temp_date = format_date(quali_date)
            temp_time = format_time(quali_time)
            self.quali_date = temp_date
            self.quali_time = temp_time
        else:
            self.quali_date = None
            self.quali_time = None
        if sprint_date != "\\N":
            temp_date = format_date(sprint_date)
            temp_time = format_time(sprint_time)
            self.sprint_date = temp_date
            self.sprint_time = temp_time
        else:
            self.sprint_date = None
            self.sprint_time = None

    def __str__(self):
        first_line = f"{self.raceId} {self.year} {self.round} {self.name} {self.date} {self.time}"
        second_line = f"{self.fp1_date} {self.fp1_time} {self.fp2_date} {self.fp2_time} {self.fp3_date} {self.fp3_time}"
        third_line = (
            f"{self.quali_date} {self.quali_time} {self.sprint_date} {self.sprint_time}"
        )
        return f"{first_line}\n{second_line}\n{third_line}"

    def race_model_dict(self):
        return {
            "race_id": self.raceId,
            "year": self.year,
            "round": self.round,
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "url": self.url,
            "fp1_date": self.fp1_date,
            "fp1_time": self.fp1_time,
            "fp2_date": self.fp2_date,
            "fp2_time": self.fp2_time,
            "fp3_date": self.fp3_date,
            "fp3_time": self.fp3_time,
            "quali_date": self.quali_date,
            "quali_time": self.quali_time,
            "sprint_date": self.sprint_date,
            "sprint_time": self.sprint_time
        }


class QualifyingTable:
    def __init__(
        self, qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3
    ):
        self.qualifyId = qualifyId
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.number = number
        self.position = position

        if q1 != "\\N":
            self.q1 = q1
        else:
            self.q1 = ""

        if q2 != "\\N":
            self.q2 = q2
        else:
            self.q2 = ""

        if q3 != "\\N":
            self.q3 = q3
        else:
            self.q3 = ""

    def __str__(self):
        return f"{self.number} {self.position} {self.q1} {self.q2} {self.q3}"

    def qualifying_model_dict(self):
        return {
            "qualify_id": self.qualifyId,
            "number": self.number,
            "position": self.position,
            "q1": self.q1,
            "q2": self.q2,
            "q3": self.q3
        }


class SprintResultTable:
    def __init__(
        self,
        resultId,
        raceId,
        driverId,
        constructorId,
        number,
        grid,
        position,
        positionText,
        positionOrder,
        points,
        laps,
        time,
        milliseconds,
        fastestLap,
        fastestLapTime,
        statusId,
    ):
        self.resultId = resultId
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.number = number
        self.grid = grid
        self.positionText = positionText
        self.positionOrder = positionOrder
        self.points = points
        self.laps = laps
        self.statusId = statusId

        if position != "\\N":
            self.position = position
        else:
            self.position = None

        if time != "\\N":
            self.time = time
        else:
            self.time = None

        if milliseconds != "\\N":
            self.milliseconds = milliseconds
        else:
            self.milliseconds = None

        if fastestLap != "\\N":
            self.fastestLap = fastestLap
        else:
            self.fastestLap = None

        if fastestLapTime != "\\N":
            self.fastestLapTime = fastestLapTime
        else:
            self.fastestLapTime = ""


class StatusTable:
    def __init__(self, statusId, status):
        self.statusId = statusId
        self.status = status

    def __str__(self):
        return f"{self.statusId} {self.status}"


class ResultTable:
    def __init__(
        self,
        resultId,
        raceId,
        driverId,
        constructorId,
        number,
        grid,
        position,
        positionText,
        positionOrder,
        points,
        laps,
        time,
        milliseconds,
        fastestLap,
        rank,
        fastestLapTime,
        fastestLapSpeed,
        statusId,
    ):
        self.resultId = resultId
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.number = number
        self.grid = grid
        self.positionText = positionText
        self.positionOrder = positionOrder
        self.points = points
        self.laps = laps
        self.statusId = statusId

        if position != "\\N":
            self.position = position
        else:
            self.position = None

        if time != "\\N":
            self.time = time
        else:
            self.time = None

        if milliseconds != "\\N":
            self.milliseconds = milliseconds
        else:
            self.milliseconds = None

        if fastestLap != "\\N":
            self.fastestLap = fastestLap
        else:
            self.fastestLap = None

        if rank != "\\N":
            self.rank = rank
        else:
            self.rank = None

        if fastestLapTime != "\\N":
            self.fastestLapTime = fastestLapTime
        else:
            self.fastestLapTime = ""

        if fastestLapSpeed != "\\N":
            self.fastestLapSpeed = fastestLapSpeed
        else:
            self.fastestLapSpeed = ""

    def __str__(self):
        first_line = f"{self.number} {self.grid} {self.position} {self.positionText} "
        second_line = f"{self.positionOrder} {self.points} {self.laps} {self.time} "
        third_line = f"{self.milliseconds} {self.fastestLap} {self.rank} {self.fastestLapTime} {self.fastestLapSpeed}"
        return first_line + second_line + third_line


class PitStopTable:
    def __init__(self, raceId, driverId, stop, lap, time, duration, milliseconds):
        self.raceId = raceId
        self.driverId = driverId
        self.stop = stop
        self.lap = lap
        self.time = time
        self.duration = duration
        self.milliseconds = milliseconds

    def __str__(self):
        first_line = f"{self.raceId} {self.driverId} {self.stop} {self.lap} "
        second_line = f"{self.time} {self.duration} {self.milliseconds}"
        return first_line + second_line


class LapTimeTable:
    def __init__(self, raceId, driverId, lap, position, time, milliseconds):
        self.raceId = raceId
        self.driverId = driverId
        self.lap = lap
        self.position = position
        self.time = time
        self.milliseconds = milliseconds

    def __str__(self):
        first_line = f"{self.raceId} {self.driverId} {self.lap} {self.position} "
        second_line = f"{self.time} {self.milliseconds}"
        return first_line + second_line


class DriverStandingTable:
    def __init__(
        self, driverStandingsId, raceId, driverId, points, position, positionText, wins
    ):
        self.driverStandingsId = driverStandingsId
        self.raceId = raceId
        self.driverId = driverId
        self.points = points
        self.position = position
        self.positionText = positionText
        self.wins = wins

    def __str__(self):
        first_line = f"{self.driverStandingsId} {self.raceId} {self.driverId} "
        second_line = f"{self.points} {self.position} {self.positionText} {self.wins}"
        return first_line + second_line


class ConstructorStandingTable:
    def __init__(
        self,
        constructorStandingsId,
        raceId,
        constructorId,
        points,
        position,
        positionText,
        wins,
    ):
        self.constructorStandingsId = constructorStandingsId
        self.raceId = raceId
        self.constructorId = constructorId
        self.points = points
        self.position = position
        self.positionText = positionText
        self.wins = wins

    def __str__(self):
        first_line = (
            f"{self.constructorStandingsId} {self.raceId} {self.constructorId} "
        )
        second_line = f"{self.points} {self.position} {self.positionText} {self.wins}"
        return first_line + second_line


class ConstructorResultTable:
    def __init__(self, constructorResultsId, raceId, constructorId, points, status):
        self.constructorResultsId = constructorResultsId
        self.raceId = raceId
        self.constructorId = constructorId
        self.points = points

        if status != "\\N":
            self.status = status
        else:
            self.status = ""

    def __str__(self):
        first_line = f"{self.constructorResultsId} {self.raceId} {self.constructorId} "
        second_line = f"{self.points}"
        return first_line + second_line
