import requests
import math
import csv
from .metar import Metar

class aviationWeather:
    def __init__(self):
        self.stations={}
        weatherData = requests.get(
                    "https://www.aviationweather.gov/adds/dataserver_current/current/metars.cache.csv"
                    ).content.decode('utf-8')
        for item in csv.reader(weatherData.splitlines(),delimiter=','):
            try:
                item[1]
            except IndexError:
                continue
            if item[0] == "raw_text":
                continue
            self.stations[item[1]] = Metar(item)

    def getStation(self, location):
        return self.stations[location].getAll()

    def getStationPosition(self,location,axis="both"):
        return self.stations[location].getcoordinates(axis)

    def getNearestStation(self,longitude,latitude):
        self.x1=float(longitude)
        self.y1=float(latitude)
        for station in self.stations.keys():
            print(self.stations[station].getStationName())
            self.x2=self.stations[station].getcoordinates("latitude")
            self.y2=self.stations[station].getcoordinates("longitude")
            print(self.stations[station].getcoordinates())
            if self.y2 == None or self.x2 == None:
                continue
            self.distance = math.fabs(math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))
            if self.distance > 180: #if over 180 degrees in distance, subtract from 360 to use the shorter distance around the globe.
                self.distance = 360 - self.distance

            print("Distance: " + str(self.distance))

    def getStations(self):
        return list(self.stations.keys())

