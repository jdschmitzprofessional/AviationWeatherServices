import requests
from .metar import Metar

class aviationWeather:
    def __init__(self):
        self.stations={}
        for item in requests.get(
                    "https://www.aviationweather.gov/adds/dataserver_current/current/metars.cache.csv"
                    ).content.decode('utf-8').split('\n'):
            try:
                item.split(',')[1]
            except IndexError:
                continue
            self.stations[item.split(',')[1]] = Metar(item.split(','))

    def getStation(self, location):
        return self.stations[location].getAll()

    def getStations(self):
        return list(self.stations.keys())[1:]

    def getPrecipitation(self,station):
        raw = self.stations[station].getMetarRaw()
        if "-RA" in raw or "-TS" in raw:
            return True
        else:
            return False

    def getOvercast(self,station):
        if "OVC" in self.stations[station].getMetarRaw():
            return True
        else:
            return False
