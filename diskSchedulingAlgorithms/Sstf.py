# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from typing import List
from diskSchedulingAlgorithms.Algo import abstractAlgorithm as Algorithm
from virtualMachine.DiskRequest import DiskRequest


class Sstf(Algorithm):
    # This class inherits from the Algorithm class and implements the SSTF algorithm.

    def __init__(self):
        # Constructor for the class
        self.name = "SSTF"  # Set the name of the algorithm.

    def sort(self, queue: List[DiskRequest], currentHeadPosition: int) -> List[DiskRequest]:
        # This method sorts the requests in the given list object according to the SSTF algorithm.

        lowestRange = None  # Initialize the lowest range to None.
        lowestRangeRequest = None  # Initialize the request with the lowest range to None.

        if queue:
            # If the queue is not empty, find the request with the lowest range.
            lowestRange = abs(queue[0].getNumber() - currentHeadPosition)
            lowestRangeRequest = queue[0]

            for r in queue:
                currentRange = abs(r.getNumber() - currentHeadPosition)
                if currentRange < lowestRange:
                    lowestRange = currentRange
                    lowestRangeRequest = r

            # Remove the request with the lowest range from the queue and insert it at the front.
            queue.remove(lowestRangeRequest)
            queue.insert(0, lowestRangeRequest)

        return queue 