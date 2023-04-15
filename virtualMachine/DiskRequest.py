# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

class DiskRequest:
    # This class represents a disk request.

    def __init__(self, number):
        # Constructor for the class
        self.number = number  # Set the request number.
        self.time = 0.0  # Initialize the time to 0.

    def getNumber(self):
        # This method returns the request number.
        return self.number

    def setNumber(self, number):
        # This method sets the request number.
        self.number = number

    def getTime(self):
        # This method returns the time.
        return self.time

    def setTime(self, time):
        # This method sets the time.
        self.time = time

    def __lt__(self, other):
        # This method is used for sorting the requests.
        return self.getNumber() < other.getNumber()

    def __eq__(self, other):
        # This method is used for comparing the requests.
        return self.getNumber() == other.getNumber()

    def __repr__(self):
        # This method returns a string representation of the request.
        return str(self.getNumber()) 