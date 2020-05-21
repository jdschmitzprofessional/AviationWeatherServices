
class coordinateLocation:
    def __init__(self, latitude=float, longitude=float):
        self.latitude=latitude
        self.longitude=longitude
        self.relativeDistances={}
    def getCoordinates(self):
        return {'x': self.latitude,
                'y': self.longitude}

    def setRelativeDistance(self,station,distance):
        self.relativeDistances[station] = distance

    def getRelativeDistance(self,station):
        return self.relativeDistances[station]