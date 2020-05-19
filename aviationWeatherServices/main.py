import aviationWeatherServices

k = aviationWeatherServices.aviationWeather()
print(k.getNearestStation(33,-112))
print(k.getStations())