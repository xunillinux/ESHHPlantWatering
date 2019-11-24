from Repository import Repository

class Controller:

    def __init__(self):
        self.repo = Repository()

    def AddHumidityValue(self, humidity_value):
        self.repo.AddHumidityValue(humidity_value)

    def GetHumidityValues(self):
        return self.repo.GetHumidityValues()
    

    def AddBrightnessValue(self, brightness_value):
        self.repo.AddBrightnessValue(brightness_value)
    
    def GetBrightnessValues(self):
        return self.repo.GetBrightnessValues()
    

    def AddTemperatureValue(self, temperature_value):
        self.repo.AddTemperatureValue(temperature_value)
    
    def GetTemperatureValues(self):
        return self.repo.GetTemperatureValues()
    

    def SetPhoto(self, img):
        #TODO implement saving of photo to /var/www/html/photos
        self.repo.SetPhoto("photo_path")

    def GetPhotos(self):
        return self.repo.GetPhotos()


    def SetSettings(self, humidity_threshhold, pump_water_amount):
        self.repo.SetSettings(humidity_threshhold, pump_water_amount)

    def GetSettings(self):
        return self.repo.GetSettings()