# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from typing import List

from virtualMachine.DiskRequest import DiskRequest 

class abstractAlgorithm:
    def __init__(self, name: str):
        # constructor to initialize Algorithm object with a name
        self.name = name
    
    def getName(self) -> str:
        # method to get the name of the Algorithm object
        return self.name
    
    def sort(self, queue: List[DiskRequest], currentHeadPosition: int) -> List[DiskRequest]:
        # method to sort a list of DiskRequest objects based on the current head position
        # (this is an abstract method that should be overridden by subclasses)
        pass
