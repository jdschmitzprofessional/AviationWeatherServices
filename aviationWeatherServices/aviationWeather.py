import requests
import math
import csv
from .coordinateLocation import coordinateLocation
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

    def getNearestStation(self,location=coordinateLocation):
        self.known_stations = []
        self.distances=[]
        self.x1=location.getCoordinates()['x']
        self.y1=location.getCoordinates()['y']
        for station in self.stations.keys():
            self.x2=self.stations[station].getcoordinates("latitude")
            self.y2=self.stations[station].getcoordinates("longitude")
            if self.y2 == None or self.x2 == None:
                continue
            else:
                self.known_stations.append(station)
            self.distance = math.fabs(math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))
            if self.distance > 180:
                self.distance = 360 - self.distance
            self.distances.append(self.distance)
            location.setRelativeDistance(station, self.distance)
        self.distances.sort()
        print(location.getRelativeDistance("KDVT"))
        for distance in self.distances[0:5]:
            for station in self.known_stations:
                if location.getRelativeDistance(station) == distance:
                    print(station + " distance: " + str(distance))
                    break

    def getStations(self):
        return list(self.stations.keys())

