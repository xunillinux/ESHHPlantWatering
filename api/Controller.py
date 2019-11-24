from Repository import Repository

class Controller:

    def __init__(self):
            self.repo = Repository()

    def AddHumidityValue(humidity_value):
        self.repo.AddHumidityValue(humidity_value)

    def GetHumidityValues():
        return self.repo.GetHumidityValues()
    

    def AddBrightnessValue(brightness_value):
        self.repo.AddBrightnessValue(brightness_value)
    
    def GetBrightnessValues():
        return self.repo.GetBrightnessValues()
    

    def AddTemperatureValue(temperature_value):
        self.repo.AddTemperatureValue(temperature_value)
    
    def GetTemperatureValues():
        return self.repo.GetTemperatureValues()
    

    def SetFoto(foto_path):
        #TODO implement saving of foto to /var/www/html/fotos
        self.repo.SetFoto(foto_path)

    def GetFotos():
        return self.repo.GetFotos()


    def SetSettings(humidity_threshhold, pump_water_amount):
        self.repo.SetSettings(humidity_threshhold, pump_water_amount)

    def GetSettings():
        return self.repo.GetSettings()