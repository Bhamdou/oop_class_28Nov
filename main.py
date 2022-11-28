class Weather():

    rl_humidity = 60

    def __init__(self, temperature, humidity, wind_speed, condition):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.condition = condition


    def to_fahrenheit(self):
        fahrenheit = self.temperature * 1.8 + 32
        return fahrenheit

    @staticmethod
    def to_dew_point(description, temp, relative_humidity):
        dew_point = temp - (100 - relative_humidity) / 5
        return dew_point

    @classmethod
    def to_dryness(cls):
        return 100 - cls



class ExtendedWeather(Weather):
    def __init__(self, temperature, humidity, wind_speed, condition, wind_pressure, ground_temperature):
        super().__init__(temperature, humidity, wind_speed, condition)
        self.wind_pressure = wind_pressure
        self.ground_temperature = ground_temperature


    def dekdljffjfj(self, jfjf, djjfj):
        jdsldj

        print
        rend
        


new_weather_1 = ExtendedWeather(37, 50, 7, 'sunny', 13, 12)

print(new_weather_1.wind_pressure)
print(new_weather_1.to_fahrenheit())




weather_1 = Weather(10, 8, 70, 'cloudy')

weather_2 = Weather(23, 2, 80, 'clear sky')

#print(Weather.rl_humidity)

# print(Weather.to_dew_point('static', 30, 80))

# print(Weather.to_dryness())

# print(weather_1.temperature)

# print(weather_1.to_fahrenheit())

# print(weather_2.temperature)

# print(weather_2.to_fahrenheit())


#print(weather_1.condition)





#print(to_dew_point(30, 60))