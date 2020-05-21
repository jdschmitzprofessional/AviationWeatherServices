import aviationWeatherServices

k = aviationWeatherServices.aviationWeather()
location = aviationWeatherServices.coordinateLocation(33.659217, -112.084063)
print(location.getCoordinates())
print(k.getNearestStation(location))