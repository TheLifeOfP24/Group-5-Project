"""This is the Control Panel Class"""



class ControlPanel(object):

    #Constructor
    def __init__(self) -> None:
        print("Control Panel Class")
        pass 

    def controlLights(self, livingRoom):

        print("Control Lights from Control Panel:")



    #Camera Class 
class Camera:
    #constructor
    def __init__(self, zoomLevel, Location) -> None:
        self._ZoomLevel = zoomLevel
        self._Location = Location
        pass

#DoorLick Clas
class DoorLock:
    
    def __init__(self, doorLocation, code) -> None:
        self._doorLocation = doorLocation #self. makes it an attribute
        self._code = code 
        pass

    #method to Lock door

    def Lock(self):
        print("Lock Door")

    #Method to Unlock Door

    def Unlock(self):
        print("Unlock door")

#Sensor Class
class Sensor:

#constructor
    def __init__(self,Sensor, Position) -> None:
        self._Sensor = Sensor
        self._Position = Position
        pass

#Methods 

#Detect Method
    def detect(self):
     print("Sensor detected")

    def sendStatus(self):
        print("Sensor Status Sent")

#Thermostat Class
class thermostat:

    def __init__(self, status, schedule, temperature, tempsensor) -> None:
        self._Status = status
        self._Schedule = schedule
        self._Temperature = temperature
        self._TempSensor = tempsensor
        pass

    def HeatControl(self):
        print("Control Heat")

    def AirConditioningControl(self):
     print("A/C Control")

    def setTemp(self):
        print("Temp set at °")


#AirCondition is a subclass thermostat

class AirCondition(thermostat):

   def __init__(self, status, schedule, temperature, tempsensor) -> None:
       super().__init__(status, schedule, temperature, tempsensor)
       self._setTemp = 0 

   def setTemp(self, degree):
       print("Set the AC to a level")
       self._setTemp = degree


#this is the Section that contains the Lights and Dimmable Lights CLasses 

class Lights:

    def __init__(self, color, location) -> None:
        self._Color = color #self. makes it an attribute
        self._Location = location #_location says location should private. 
        
  #Method to turn light on and off

    def turnOn(self):
        print("Turn Light On")

    def turnOff(self):
        print("Turn Light Off")


#DimmableLights is a subclass of Lights
class DimmableLights(Lights):
    def __init__(self, color, location) -> None:
        super().__init__(color, location)
        self._Brightness = 0

    def setBrightness(self,level):
        print("Sets the Light level")
        self._Brightness = level

#WiFi is a class

class WiFi:
    def __init__(self, Alert_MSG, signalType, Command) -> None:
        self._Alerts = Alert_MSG
        self._SignalType = signalType
        self.Comman = Command

    
    def sendAlert(self):
        print("Send Wifi Alert")

    def MakeVisible(self):
        print("WiFi is visible")

#Time class

class Time(object):
    def __init__(self, Hours, min) -> None:
        self._Hours = Hours
        self._min = min
    def On(self):
        print("Timer on")
    def Off(self):
        print("Time is Off")

    def setTime(self):
        print("Time is set")






ES = Time(Hours="" , min="")

ES.Off()
ES.On()
ES.setTime()