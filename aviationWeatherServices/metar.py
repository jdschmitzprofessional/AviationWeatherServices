class Metar:
    def __init__(self,inputString=list):
        self.metarRaw=inputString[0]
        self.stationName=inputString[1]
        self.zuluTime=inputString[2]
        self.latitude=inputString[3]
        self.longitude=inputString[4]
        self.tempCelsius=inputString[5]
        self.dewPoint=inputString[6]
        self.windDirection=inputString[7]
        self.windSpeedKnots=inputString[8]
        self.gustSpeedKnots=inputString[9]
        self.visibility=inputString[10]
        self.altim_in_hg=inputString[11]
        self.sea_level_pressure_mb=inputString[12]
        self.corrected=inputString[13]
        self.auto=inputString[14]
        self.auto_station=inputString[15]
        self.maintenance_indicator_on=inputString[16]
        self.no_signal=inputString[17]
        self.lightning_sensor_off=inputString[18]
        self.freezing_rain_sensor_off=inputString[19]
        self.present_weather_sensor_off=inputString[20]
        self.wx_string=inputString[21]
        self.sky_cover=inputString[22]
        self.cloud_base_ft_agi=inputString[23]
        self.sky_cover_2=inputString[24]
        self.cloud_base_ft_agi_2=inputString[25]
        self.sky_cover_3=inputString[26]
        self.cloud_base_ft_agi_3=inputString[27]
        self.flight_category=inputString[28]
        self.three_hr_pressure_tendency_mb=inputString[29]
        self.maxT_c = inputString[30]
        self.minT_c = inputString[31]
        self.maxT24hr_c = inputString[32]
        self.minT24hr_c = inputString[33]
        self.precip_in = inputString[34]
        self.pcp3hr_in = inputString[35]
        self.pcp6hr_in = inputString[36]
        self.pcp24hr_in = inputString[37]
        self.snow_in = inputString[38]
        self.vert_vis_ft = inputString[39]
        self.metar_type = inputString[40]
        self.elevation_m = inputString[41]
        self.relativeDistance = None

    def getAll(self):
        return self.__dict__

    def getcoordinates(self,axis="both"):
        if axis == "both":
            if self.latitude == (None or "") or self.longitude == (None or ""):
                return None
            return [ float(self.latitude), float(self.longitude) ]
        elif axis == "latitude":
            if self.latitude == (None or ""):
                return None
            return float(self.latitude)
        elif axis == "longitude":
            if self.longitude == (None or ""):
                return None
            return float(self.longitude)

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