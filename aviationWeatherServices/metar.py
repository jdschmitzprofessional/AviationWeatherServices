class Metar:
    def __init__(self,inputString=list):
        self.metarRaw=inputString[0]
        self.stationName=inputString[1]
        self.zuluTime=inputString[2]
        self.tempCelsius=inputString[5]
        self.dewPoint=inputString[6]
        self.windDirection=inputString[7]
        self.windSpeedKnots=inputString[8]
        self.gustSpeedKnots=inputString[9]
        self.visibility=inputString[10]
    def getAll(self):
        print("Metar raw: %s\nstationName: %s\nzuluTime: %s\ntempCelsius: %s\ndewPoint: %s\n"
              "windDirection: %s\nwindSpeedKnots: %s\ngustSpeedKnots: %s\nvisbility: %s"%(
            self.metarRaw,self.stationName,self.zuluTime,self.tempCelsius,self.dewPoint,self.windDirection,
            self.windSpeedKnots,self.gustSpeedKnots,self.visibility))
    def getMetarRaw(self):
        return self.metarRaw
    def getStationName(self):
        return self.stationName
    def getZuluTime(self):
        return self.zuluTime
    def getTempCelsius(self):
        return self.tempCelsius
    def getDewPoint(self):
        return self.dewPoint
    def getWindDirection(self):
        return self.windDirection
    def getWindSpeedKnots(self):
        return self.windSpeedKnots
    def getGustSpeedKnots(self):
        return self.gustSpeedKnots
    def getVisibility(self):
        return self.visibility