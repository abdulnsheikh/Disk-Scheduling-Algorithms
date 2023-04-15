# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

class TheDisk:
    START_CYLINDER = 0   # Starting cylinder of the disk
    
    def __init__(self):
        # Initializes default values for various properties
        self.cylinders = 1024    # Total number of cylinders in the disk
        self.speed = 7200        # Disk speed in RPM
        self.startDelay = 1      # Delay time before disk starts moving
        self.stopDelay = 1       # Delay time after disk stops moving
        self.timeToTravel = 0.15 # Time required for the head to move from one cylinder to another
        self.latency = 4.2       # Time required for the head to reach the desired cylinder
        self.currentHeadPosition = TheDisk.START_CYLINDER  # Current head position
    
    # Getters and setters for various properties
    def getCylinders(self):
        return self.cylinders
    
    def setCylinders(self, cylinders):
        self.cylinders = cylinders
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def getStartDelay(self):
        return self.startDelay
    
    def setStartDelay(self, startDelay):
        self.startDelay = startDelay
    
    def getStopDelay(self):
        return self.stopDelay
    
    def setStopDelay(self, stopDelay):
        self.stopDelay = stopDelay
    
    def getTimeToTravel(self):
        return self.timeToTravel
    
    def setTimeToTravel(self, timeToTravel):
        self.timeToTravel = timeToTravel
    
    def getLatency(self):
        return self.latency
    
    def setLatency(self, latency):
        self.latency = latency
    
    def getCurrentHeadPosition(self):
        return self.currentHeadPosition
    
    def setCurrentHeadPosition(self, currentHeadPosition):
        self.currentHeadPosition = currentHeadPosition
    
    # Calculates the distance between two cylinders
    def getCylinderDistance(self, startCylinder, stopCylinder):
        return abs(startCylinder - stopCylinder)
    
    # Calculates the seek time required to move the head from startCylinder to stopCylinder
    def getSeekTime(self, startCylinder, stopCylinder):
        if startCylinder == stopCylinder:
            # If both start and stop cylinders are same, only latency time is required
            return self.getLatency()

        calculation = self.calculateSeekTime(startCylinder, stopCylinder)
        return self.roundToTwoDecimalPlaces(calculation)
    
    # Calculates the seek time required to move the head from startCylinder to stopCylinder
    def calculateSeekTime(self, startCylinder, stopCylinder):
        return self.getStartDelay() + (self.getCylinderDistance(startCylinder, stopCylinder) * self.getTimeToTravel()) + self.getStopDelay() + self.getLatency()
    
    # Rounds the value to two decimal places
    def roundToTwoDecimalPlaces(self, value):
        return round(value, 2)
