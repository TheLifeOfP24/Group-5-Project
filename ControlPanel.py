"""This is the Control Panel Class"""



class ControlPanel(object):

    #Constructor
    def __init__(self, LCD, AlertMessage) -> None:
        self._LCD = LCD
        self._AlertMessage =AlertMessage
        print("Welcome Home")
        pass 

    def controlLights(self):

        print("Light is turned on - will turn off at 7:00PM:")

    def checkStatus(self):
        print("Camera motion detected")

    def checkWifi(self):
        print("Wifi connection secured")
    
    def controlTemperature(self):
        print("Temperature is set to 69°")

    def controlDoorLock(self):
        print("door Is locked")

    def connectDevice(self):
        print("Device connected")

    def allControl(self):
        print("All controlls")

    def setTask(self):
        print("sending command")

idle = ControlPanel(LCD="" , AlertMessage="")

idle.checkStatus()
idle.checkWifi()
idle.controlLights()
idle.controlTemperature()
idle.controlDoorLock()
idle.setTask()

    #Camera Class 
class Camera:
    #constructor
    def __init__(self, zoomLevel, Location) -> None:
        self._ZoomLevel = zoomLevel
        self._Location = Location
        pass


class NightVision(Camera):
    def __init__(self, zoomLevel, Location) -> None:
        super().__init__(zoomLevel, Location)
        self._setLevel = 0

    def detectVisibility(self):
        print("Visibility detected")

    def autoOn(self):
        print("Night vision is on")

    def autoOff(self):
        print("Night Visiton is Off")

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

    def __init__(self, Speed, Schedule, temperature) -> None:
        self._speed = Speed
        self._Schedule = Schedule
        self._Temperature = temperature
        pass

    def turnOnSystem(self):
        print("System Turned On")

    def turnOffSystem(self):
     print("System Turned Off")

    def setSchedule(self):
        print("Schedule Set")

    def setTemp(self):
        print("Temp set at °")


class EvaporatorUnit:

    def __init__(self, speed, schedule) -> None:
        self._speed = speed
        self._schedule = schedule
        pass

    def turnOn(self):
        print("Turned On")

    def turnOff(self):
        print("Turned Off")

    def setSchedule(self):
        print("Schedule Set")

    def setSpeed(self):
        print("speed set")

class HVAC:

    def __init__(self, status, schedule, tempSensor) -> None:
        self._status = status
        self._schedule = schedule
        self._tempSensor = tempSensor
        pass

    def heatControl(self):
        print("Control heat")

    def AirConditioningControl(self):
        print("Control Air Conditioning")

    def setDefrostMode(self):
        print("set the defrost mode")


#AirCondition

class AirCondition(HVAC):

   def __init__(self, status, schedule, tempsensor) -> None:
       super().__init__(status, schedule, tempsensor)
       self._setTemp = 0 

   def setTemp(self, degree):
       print("Set the AC to a level")
       self._setTemp = degree

class Heater(HVAC):
    def __init__(self, status, schedule, tempSensor) -> None:
        super().__init__(status, schedule, tempSensor)
        self._setTemp = 0

    def turnOn(self):
        print("Turn ON")

    def turnOff(self):
        print("Turn Off")

    def heat(self):
        print("Set heat temp to ")

class CondenserUnit(HVAC):

    def __init__(self, status, schedule, tempSensor) -> None:
        super().__init__(status, schedule, tempSensor)
        self._setSpeed = 0 

    def turnOn(self):
        print("Turn on COndenser Unit")

    def turnOff(self):
        print("Turn off Condenser Unit")

    def setSpeed(self):
        prtin("speed set")

class Compressor(CondenserUnit):

    def __init__(self, status, schedule, tempSensor, OilLevel, Capacitator, ElectroFan, GasLevel) -> None:
        self._oilLevel = OilLevel
        self._capacitator = Capacitator
        self._ElectroFan = ElectroFan
        self._GasLevel = GasLevel
        super().__init__(status, schedule, tempSensor)

    def turnOn(self):
        print("Turn On")

    def turnOff(self):
        print("Turn Off")

    def FreqRegMotor(self):
        print("Frequence Requlation Motor Turned ON")

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

class Timer(object):
    def __init__(self, Hours, min) -> None:
        self._Hours = Hours
        self._min = min
    def On(self):
        print("Timer on")
    def Off(self):
        print("Time is Off")

    def setTime(self):
        print("Time is set")






